__all__ = ['PwnlibException']
import traceback, sys

class PwnlibException(Exception):
    '''Exception thrown by the pwnlib thrown by :func:`pwnlib.log.error`
    (we are in :data:`pwnlib.term.term_mode`, in which case the
    function will simply exit).

    Pwnlib functions that encounters unrecoverable errors should call the
    :func:`pwnlib.log.error` function instead of throwing this exception directly.'''
    def __init__(self, msg, reason = None, exit_code = None):
        '''bar'''
        Exception.__init__(self, msg)
        self.reason = reason
        self.exit_code = exit_code

    def __repr__(self):
        s = 'PwnlibException: %s' % self.message
        if self.reason:
            s += '\nReason:\n'
            s += ''.join(traceback.format_exception(*self.reason))
        elif sys.exc_type not in [None, KeyboardInterrupt]:
            s += '\n'
            s += ''.join(traceback.format_exc())
        return s
