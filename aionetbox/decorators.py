import functools
import itertools
import logging

import asyncio

LOG = logging.getLogger(__name__)

def retry_request(*, exceptions=(), delays=None):
    """Retries http requests if specified errors occur.
    Args:
        delays (tuple): Series of durations (in seconds) to wait between retries.
        exceptions (tuple): list of exceptions to intercept and allow retry.
    Returns:
        decorator (func): the actual decorator
    """
    if delays is None:
        delays = (0, .5, .75, 1, 2)

    def decorator(func):
        """Retries requests
        Args: func (func): function calling http request
        Returns:
            func: the decorated function
        """
        @functools.wraps(func)
        async def retry_handled(*args, **kwargs):
            """Executes function
            Returns:
                results of the wrapped function
            Raises:
                the original exception if request fails all retries
            """
            errors = []
            # append sentinel None to delays chain to serve as exit condition
            for delay in itertools.chain(delays, [None]):
                try:
                    return await func(*args, **kwargs)
                except exceptions as error:
                    errors.append(error)
                    if delay is None:  # exit condition from sentinel None
                        LOG.error(
                            'request %s failed definitely: %s',
                            func.__name__, errors)
                        raise error
                    else:
                        LOG.warning(
                            'request %s failed: %s',
                            func.__name__, error)
                        await asyncio.sleep(delay)
        return retry_handled
    return decorator
