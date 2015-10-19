a quick intro to complexity and ctypes
--------------------------------------


Big-O notation

* O(n^2) -- slow
* O(n) -- not so fast
* O(log n) -- pretty good
* O(1) -- FAST


Some simple examples (in python):

* `n_squared`
* `linear`
* `log_n`


Plotting some run time results (using the ipython shell)


    >>> import main
    >>> %pylab
    >>>
    >>> # Time some stuff
    >>> n2_results = main.time_complexity('n_squared', 100)
    >>> n_results = main.time_complexity('linear', 100)
    >>> log_results = main.time_complexity('log_n', 100)
    >>>
    >>> # Plot them:
    >>> plot(log_results)
    >>> plot(n_results)
    >>> plot(n2_results)

Now, Look at the C implementations.

1. Structure: header file, implementation file
2. the Makefile
3. The `main` app (just to see that things work)

Now, use _ctypes_ to call this code from python, and re-run the timing results.


    >>> # Time the c code
    >>> cn2_results = main.time_complexity('c_n_squared', 100)
    >>> cn_results = main.time_complexity('c_linear', 100)
    >>> clog_results = main.time_complexity('c_log_n', 100)
    >>>
    >>> # Plot them:
    >>> plot(c_log_results)
    >>> plot(c_n_results)
    >>> plot(c_n2_results)

Nifty!
