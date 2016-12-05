#coding: utf-8
from __future__ import unicode_literals, absolute_import
import logging
from datetime import timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.util import timedelta_seconds
from django.utils import timezone
from django.db import transaction
from .remind import Remind

logger = logging.getLogger(__name__)


class RemindScheduler(BackgroundScheduler):
    misfire_grace_time = 60
    MAX_WAIT_TIME = 60*60  # wake up every hour

    def _process_jobs(self):
        """Goodbye you apscheduler"""
        logger.debug('Looking for jobs to run')
        try:
            now = timezone.now()
            grace_time = timedelta(seconds=self.misfire_grace_time)

            with self._jobstores_lock:
                with transaction.atomic():
                    # Lock the row
                    for rem in Remind.objects.select_for_update().filter(
                            done=False, notify_time__range=(now-grace_time, now)).all():
                        rem.notify_users()
                        rem.done = True
                        rem.save(update_fields=['done'])
                    next_remind = Remind.objects.filter(
                        done=False, notify_time__gt=now-grace_time).order_by('notify_time').first()
                    wait_seconds = None
                    if next_remind:
                        wait_seconds = max(timedelta_seconds(next_remind.notify_time - timezone.now()), 0)
                        logger.debug('Next wake up is due at %s (in %f seconds)', next_remind.notify_time.isoformat(), wait_seconds)
                    else:
                        logger.debug('No jobs, waiting until a job is added')
                    return wait_seconds
        # This is a vital thread, DO NOT die
        except Exception as e:
            logger.exception('Error running scheduler job')

