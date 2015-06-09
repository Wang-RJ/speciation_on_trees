from numpy import *
from evcEqsEPL import *

import scipy.optimize

# guesser used to initialize parameters for optimization under
# different models

def n3_guesser(obs, K_1, K_2):
    guesses = array([ 3 * float(obs[0]) / (4 * K_2**3),
                      3 * float(obs[1]) / (4 * (K_1 + K_2)**3),
                      3 * float(obs[2]) / (4 * (K_1 + K_2)**3),
                      6 * float(obs[3]) / (2*K_1 + K_2)**3,
                      6 * float(obs[4]) / K_2**3,
                      6 * float(obs[5]) / K_2**3 ])

    guess = average(missV_wrap(guesses, guesses))

    if(guess <= 0):
        guess = 1e-10

    return guess

def n2_guesser(obs, K_1, K_2):
    guesses = array([ float(obs[0]) / (2*K_2**2),
                      float(obs[1]) / (2 * (K_1 + K_2)**2),
                      float(obs[2]) / (2 * (K_1 + K_2)**2),
                      2 * float(obs[3]) / (2*K_1 + K_2)**2,
                      2 * float(obs[4]) / K_2**2,
                      2 * float(obs[5]) / K_2**2 ])

    guess = average(missV_wrap(guesses, guesses))

    if(guess <= 0):
        guess = 1e-10

    return guess
    
def n1_guesser(obs, K_1, K_2):
    guesses = array([ float(obs[0]) / (2*K_2),
                      float(obs[1]) / (2 * (K_1+K_2)),
                      float(obs[2]) / (2 * (K_1+K_2)),
                      float(obs[3]) / (2*K_1 + K_2),
                      float(obs[4]) / K_2,
                      float(obs[5]) / K_2 ])

    guess = average(missV_wrap(guesses, guesses))
    if(guess <= 0):
        guess = 1e-10

    return guess

def n2_dadd_guesser(obs, K_1, K_2):
    mat = array([
        [K_2**2, K_2**2],
        [(K_1+K_2)**2, (K_1+K_2)**2],
        [(K_1+K_2)**2, (K_1+K_2)**2],
        [K_1**2+K_1*K_2+(1./2)*K_2**2, K_1**2+K_1*K_2],
        [(1./2)*K_2**2, 0],
        [(1./2)*K_2**2, 0]])

    guess = dot(linalg.pinv(mat), obs)

    if(guess[1] <= 0):
        guess[1] = 1e-10  # 1e-10 is the lower boundary value on guess for
    if(guess[0] <= 0):    # the maxprob, guess 0 and the gradient will
        guess[0] = 1e-10  # screw up

    return guess

# maxprob functions maximize likelihood under different models

def maxprob_n3(K_1, K_2, obs):
    p_guess = n3_guesser(obs, K_1, K_2)

    x_0 = array([ p_guess ])
    scale = x_0

    fun = lambda *args: -log_likelihood_n3(args[0] * scale, args[1], args[2], args[3])

    x = scipy.optimize.fmin_l_bfgs_b(fun, (x_0 / scale), args = (K_1, K_2, obs),
                                     bounds = [(1e-18 / scale[0], 1 / scale[0])],
                                     approx_grad = True)
    return (-x[1], x[0] * scale)

def maxprob_n2(K_1, K_2, obs):                                
    p_guess = n2_guesser(obs, K_1, K_2)
    
    x_0 = array([ p_guess ])
    scale = x_0

    fun = lambda *args: -log_likelihood_n2(args[0] * scale, args[1], args[2], args[3])

    x = scipy.optimize.fmin_l_bfgs_b(fun, (x_0 / scale), args = (K_1, K_2, obs),
                                     bounds = [(1e-15 / scale[0], 1 / scale[0])],
                                     approx_grad = True)

    return (-x[1], x[0] * scale)


def maxprob_n1(K_1, K_2, obs, lower_eps = 1e-4, upper_eps = 1):
    p_guess = n1_guesser(obs, K_1, K_2)

    x_0 = array([ p_guess, 1 ])
    scale = x_0

    fun = lambda *args: -log_likelihood_n1(args[0] * scale, args[1], args[2], args[3])

    x = scipy.optimize.fmin_l_bfgs_b(fun, (x_0 / scale), args = (K_1, K_2, obs),
                                     bounds = [(1e-6 / scale[0], 1/scale[0]),
                                               (lower_eps / scale[1], upper_eps / scale[1])],
                                     approx_grad = True)

    return (-x[1], x[0] * scale)

def maxprob_n2n3(K_1, K_2, obs):
    p2_guess = n2_guesser(obs, K_1, K_2)
    p3_guess = n3_guesser(obs, K_1, K_2)

    x_0 = array([ p2_guess, p3_guess ])
    scale = x_0

    fun = lambda *args: -log_likelihood_n2n3(args[0] * scale, args[1], args[2], args[3])

    x = scipy.optimize.fmin_l_bfgs_b(fun, (x_0 / scale), args = (K_1, K_2, obs),
                                     bounds = [(1e-15 / scale[0], 1/scale[0]),
                                               (1e-18 / scale[1], 1/scale[1])],
                                     approx_grad = True)

    return (-x[1], x[0] * scale)

def maxprob_n2_dadd(K_1, K_2, obs):
    p_guess = n2_dadd_guesser(obs, K_1, K_2)

    x_0 = array([ p_guess[0], p_guess[1] ])
    scale = x_0

    fun = lambda *args: -log_likelihood_n2_dadd(args[0] * scale, args[1], args[2], args[3])

    x = scipy.optimize.fmin_l_bfgs_b(fun, (x_0 / scale), args = (K_1, K_2, obs),
                                     bounds = [(1e-15 / scale[0], 1e-6/scale[0]),
                                               (1e-15 / scale[1], 1e-6/scale[1])],
                                     approx_grad = True)
    
    return (-x[1], x[0] * scale)
