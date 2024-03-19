""" This is the class for a timing function.
"""
import time
######################################################################
## TIMER CLASS
class DABTimer():
    """ This is the class for a timing function.
    """
    def __init__(self):
#        self._time_cpu_prev = time.clock()
        self._time_cpu_prev = time.perf_counter()
        self._time_wallclock_begin = time.time()
        self._time_wallclock_prev = self._time_wallclock_begin

######################################################################
    def timecall(self, label):
        """ This prints out the time.
        Parameters:
            label: a label to label the timer output with.
        Returns:
            outstring: the string version of what is to be printed.
        """
#        time_cpu_next = time.clock()
        time_cpu_next = time.perf_counter()
        time_wallclock_next = time.time()
        time_cpu = time_cpu_next - self._time_cpu_prev
        time_wallclock_current = time_wallclock_next - \
                   self._time_wallclock_prev
        time_wallclock_total = time_wallclock_next - \
                   self._time_wallclock_begin

        if time_wallclock_current > 0.0:
            percent = 100.00 * (time_cpu / time_wallclock_current)
            percent = min(percent, 100.00)

        outstring = 'TIME*******************************************************************\n'
        outstring += f'TIME {label:<20s} {percent:7.3f}  {time_cpu:10.3f} user'
        outstring += f'   {time_wallclock_current:10.3f} wall\n'

        outstring += f'TIME {label:<20s}          {time_cpu_next:10.3f} user_t'
        outstring += f' {time_wallclock_total:10.3f} wall_t\n'
        outstring += 'TIME*******************************************************************'

        self._time_cpu_prev = time_cpu_next
        self._time_wallclock_prev = time_wallclock_next

        # return the output string
        # and [cpu time of this interval,  cpu time total]
        return outstring
