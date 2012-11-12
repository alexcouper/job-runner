from datetime import datetime

from django.test import TestCase

from job_runner.apps.job_runner.models import Run


class RunManagerTestCase(TestCase):
    """
    Tests for the job run manager.
    """
    fixtures = ['test_job']

    def test_awaiting_enqueue(self):
        """
        Test :meth:`.Run.awaiting_enqueue`.
        """
        self.assertEqual(1, Run.objects.awaiting_enqueue().count())

        run = Run.objects.get(pk=1)
        run.enqueue_dts = datetime.now()
        run.save()

        self.assertEqual(0, Run.objects.awaiting_enqueue().count())
