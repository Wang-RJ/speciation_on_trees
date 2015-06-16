from numpy import *

def Ex_n1(p_1, K_1, K_2):
    return array([2*p_1*K_2,          # ab
                  2*p_1*(K_1+K_2),    # ac
                  2*p_1*(K_1+K_2),    # bc
                  p_1*(2*K_1+K_2),    # shC
                  p_1*K_2,            # shB
                  p_1*K_2])            # shA

def der_Ex_n1(p_1, K_1, K_2):
    return array([2*K_2,
                  2*(K_1+K_2),
                  2*(K_1+K_2),
                  (2*K_1+K_2),
                  K_2,
                  K_2])

def Ex_n2(p_2, K_1, K_2):
    return array([2*p_2*K_2**2,
                  2*p_2*(K_1+K_2)**2,
                  2*p_2*(K_1+K_2)**2,
                  (1./2)*p_2*(2*K_1+K_2)**2,
                  (1./2)*p_2*(K_2)**2,
                  (1./2)*p_2*(K_2)**2])

def Ex_n2_dadd(p_a, p_d, K_1, K_2):
    return array([(p_a+p_d)*K_2**2,
                  (p_a+p_d)*(K_1+K_2)**2,
                  (p_a+p_d)*(K_1+K_2)**2,
                  (p_a+p_d)*(K_1**2+K_1*K_2)+(1./2)*p_a*K_2**2,
                  (1./2)*p_a*K_2**2,
                  (1./2)*p_a*K_2**2])

def der_Ex_n2(p_2, K_1, K_2):
    return array([2*K_2**2,
                  2*(K_1+K_2)**2,
                  2*(K_1+K_2)**2,
                  (1./2)*(2*K_1+K_2)**2,
                  (1./2)*K_2**2,
                  (1./2)*K_2**2])

def Ex_n3(p_3, K_1, K_2):
    return array([(4./3)*p_3*K_2**3,
                  (4./3)*p_3*(K_1+K_2)**3,
                  (4./3)*p_3*(K_1+K_2)**3,
                  (1./6)*p_3*(2*K_1+K_2)**3,
                  (1./6)*p_3*K_2**3,
                  (1./6)*p_3*K_2**3])

def der_Ex_n3(p_3, K_1, K_2):
    return array([(4./3)*K_2**3,
                  (4./3)*(K_1+K_2)**3,
                  (4./3)*(K_1+K_2)**3,
                  (1./6)*(2*K_1+K_2)**3,
                  (1./6)*K_2**3,
                  (1./6)*K_2**3])

def Ex_n1n2(p_1, p_2, K_1, K_2):
    return list(array(Ex_n1(p_1, K_1, K_2)) + array(Ex_n2(p_2, K_1, K_2)))

def Ex_n2n3(p_2, p_3, K_1, K_2):
    return list(array(Ex_n2(p_2, K_1, K_2)) + array(Ex_n3(p_3, K_1, K_2)))

def Var_n1(p_1, K_1, K_2):
    return Ex_n1(p_1, K_1, K_2)

def der_Var_n1(p_1, K_1, K_2):
    return der_Ex_n1(p_1, K_1, K_2)

def der2_Var_n1(p_1, K_1, K_2):
    return array([0,0,0,0,0,0])

def Var_n2(p_2, K_1, K_2):
    return array([2*p_2*K_2**2*(1+4*p_2*K_2),
                  2*p_2*(K_1+K_2)**2*(1+4*p_2*(K_1+K_2)),
                  2*p_2*(K_1+K_2)**2*(1+4*p_2*(K_1+K_2)),
                  (1./2)*p_2*(2*K_1+K_2)**2*(1+2*p_2*(2*K_1+K_2)),
                  (1./2)*p_2*K_2**2*(1+2*p_2*K_2),
                  (1./2)*p_2*K_2**2*(1+2*p_2*K_2)])

def Var_n2_dadd(p_a, p_d, K_1, K_2):
    return array([(p_a+p_d)*K_2**2*(1+2*K_2*(p_a+p_d)),
                  (p_a+p_d)*(K_1+K_2)**2*(1+2*(p_a+p_d)*(K_1+K_2)),
                  (p_a+p_d)*(K_1+K_2)**2*(1+2*(p_a+p_d)*(K_1+K_2)),
                  (1./2)*(p_a*K_2**2*(1+2*K_2*p_a)+4*K_1**3*(p_a+p_d)**2+
                          2*K_1*K_2*(p_a+3*K_2*p_a**2+p_d+2*K_2*p_a*p_d+K_2*p_d**2)+
                          2*K_1**2*(p_a+p_d)*(1+3*K_2*(p_a+p_d))),
                  (1./2)*(p_a*K_2**2)*(1+2*p_a*K_2),
                  (1./2)*(p_a*K_2**2)*(1+2*p_a*K_2)])

def der_Var_n2(p_2, K_1, K_2):
    return array([2*K_2**2*(1+8*p_2*K_2),
                  2*(K_1+K_2)**2*(1+8*p_2*(K_1+K_2)),
                  2*(K_1+K_2)**2*(1+8*p_2*(K_1+K_2)),
                  (1./2)*(2*K_1+K_2)**2*(1+8*p_2*K_1+4*p_2*K_2),
                  (1./2)*K_2**2*(1+4*p_2*K_2),
                  (1./2)*K_2**2*(1+4*p_2*K_2)])

def der2_Var_n2(p_2, K_1, K_2):
    return array([16*K_2**3,
                  16*(K_1+K_2)**3,
                  16*(K_1+K_2)**3,
                  2*(2*K_1+K_2)**3,
                  2*K_2**3,
                  2*K_2**3])
                      
def Var_n3(p_3, K_1, K_2):
    return array([(4./3)*p_3*K_2**3*(1+6*p_3*K_2*(1+K_2)),
                  (4./3)*p_3*(K_1+K_2)**3*(1+6*p_3*(K_1+K_2)*(1+K_1+K_2)),
                  (4./3)*p_3*(K_1+K_2)**3*(1+6*p_3*(K_1+K_2)*(1+K_1+K_2)),
                  (1./12)*p_3*(2*K_1+K_2)**3*(2+3*p_3*(2*K_1+K_2)*(2+2*K_1+K_2)),
                  (1./12)*p_3*K_2**3*(2+3*p_3*K_2*(2+K_2)),
                  (1./12)*p_3*K_2**3*(2+3*p_3*K_2*(2+K_2))])

def der_Var_n3(p_3, K_1, K_2):
    return array([(4./3)*K_2**3*(1+12*p_3*K_2*(1+K_2)),
                  (4./3)*(K_1+K_2)**3*(1+12*p_3*(K_1+K_2)*(1+K_1+K_2)),
                  (4./3)*(K_1+K_2)**3*(1+12*p_3*(K_1+K_2)*(1+K_1+K_2)),
                  (1./6)*(2*K_1+K_2)**3*(1+3*p_3*(2*K_1+K_2)*(2+2*K_1+K_2)),
                  (1./6)*K_2**3*(1+3*p_3*K_2*(2+K_2)),
                  (1./6)*K_2**3*(1+3*p_3*K_2*(2+K_2))])

def der2_Var_n3(p_3, K_1, K_2):
    return array([(4./3)*K_2**4*(1+K_2),
                  16*(K_1+K_2)**4*(1+K_1+K_2),
                  16*(K_1+K_2)**4*(1+K_1+K_2),
                  (1./2)*(2*K_1+K_2)**4*(2+2*K_1+K_2),
                  (1./2)*K_2**4*(2+K_2),
                  (1./2)*K_2**4*(2+K_2)])

def Var_n1n2(p_1, p_2, K_1, K_2):
    return list(array(Var_n1(p_1, K_1, K_2)) +
                array(Var_n2(p_2, K_1, K_2)) +
                [8*p_1*p_2*K_2**2,
                 8*p_1*p_2*(K_1+K_2)**2,
                 8*p_1*p_2*(K_1+K_2)**2,
                 2*p_1*p_2*(2*K_1+K_2)**2,
                 2*p_1*p_2*K_2**2,
                 2*p_1*p_2*K_2**2])

def Var_n2n3(p_2, p_3, K_1, K_2):
    return list(array(Var_n2(p_2, K_1, K_2)) +
                array(Var_n3(p_3, K_1, K_2)) +
                [8*p_2*p_3*K_2**3*(1+2*K_2),
                 8*p_2*p_3*(K_1+K_2)**3*(1+2*K_1+2*K_2),
                 8*p_2*p_3*(K_1+K_2)**3*(1+2*K_1+2*K_2),
                 p_2*p_3*(1+2*K_1+K_2)*(2*K_1+K_2)**3,
                 p_2*p_3*K_2**3*(1+K_2),
                 p_2*p_3*K_2**3*(1+K_2)])

def Cov_n1(p_1, K_1, K_2):
    return array([p_1*K_2,            #abac
                  p_1*K_2,            #abbc
                  p_1*K_2,            #abshb
                  p_1*K_2,            #absha
                  p_1*K_2,            #bcshb
                  p_1*K_2,            #acsha
                  p_1*(2*K_1+K_2),    #acshc
                  p_1*(2*K_1+K_2),    #bcshc
                  p_1*(2*K_1+K_2),    #acbc
                  0,                  #abshc
                  0,                  #acshb
                  0,                  #bcsha
                  0,                  #shcshb
                  0,                  #shcsha
                  0])                 #shbsha

def der_Cov_n1(p_1, K_1, K_2):
    return array([K_2,
                  K_2,
                  K_2,
                  K_2,
                  K_2,
                  K_2,
                  2*K_1+K_2,
                  2*K_1+K_2,
                  2*K_1+K_2,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0])

def der2_Cov_n1(p_1, K_1, K_2):
    return array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

def Cov_n2(p_2, K_1, K_2):
    return array([(p_2/2.)*K_2**2*(1+8*p_2*(K_1+K_2)),
                  (p_2/2.)*K_2**2*(1+8*p_2*(K_1+K_2)),
                  (p_2/2.)*K_2**2*(1+4*p_2*K_2),
                  (p_2/2.)*K_2**2*(1+4*p_2*K_2),
                  (p_2/2.)*K_2**2*(1+4*p_2*(K_1+K_2)),
                  (p_2/2.)*K_2**2*(1+4*p_2*(K_1+K_2)),
                  (p_2/2.)*(2*K_1+K_2)**2*(1+4*p_2*(K_1+K_2)),
                  (p_2/2.)*(2*K_1+K_2)**2*(1+4*p_2*(K_1+K_2)),
                  (p_2/2.)*(2*K_1+K_2)*(8*p_2*K_1**2+(2*K_1+K_2)*(1+8*p_2*K_2)),
                  0,
                  0,
                  0,
                  0,
                  0,
                  0])

def Cov_n2_dadd(p_a, p_d, K_1, K_2):
    return array([(1./2)*K_2**2*(2*p_a**2*(K_1+K_2)+2*p_d**2*(K_1+K_2)+p_a*(1+4*p_d*(K_1+K_2))),
                  (1./2)*K_2**2*(2*p_a**2*(K_1+K_2)+2*p_d**2*(K_1+K_2)+p_a*(1+4*p_d*(K_1+K_2))),
                  (1./2)*K_2**2*p_a*(1+2*K_2*(p_a+p_d)),
                  (1./2)*K_2**2*p_a*(1+2*K_2*(p_a+p_d)),
                  (1./2)*K_2**2*p_a*(1+2*(K_1+K_2)*(p_a+p_d)),
                  (1./2)*K_2**2*p_a*(1+2*(K_1+K_2)*(p_a+p_d)),
                  (1./2)*(K_2**2*p_a+2*K_1**2*(p_a+p_d)+2*K_1*K_2*(p_a+p_d))*(1+2*(K_1+K_2)*(p_a+p_d)),
                  (1./2)*(K_2**2*p_a+2*K_1**2*(p_a+p_d)+2*K_1*K_2*(p_a+p_d))*(1+2*(K_1+K_2)*(p_a+p_d)),
                  (1./2)*p_a*(2*K_1**2+2*K_1*K_2+K_2**2+2*(K_1+K_2)**2*(2*K_1+K_2)*p_a)+
                  (K_1+K_2)*(K_1+2*(K_1+K_2)*(2*K_1+K_2)*p_a)*p_d+p_d**2*(2*K_1+K_2)*(K_1+K_2)**2,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0])

def der_Cov_n2(p_2, K_1, K_2):
    return array([(1./2)*K_2**2*(1+16*p_2*(K_1+K_2)),
                  (1./2)*K_2**2*(1+16*p_2*(K_1+K_2)),
                  (1./2)*K_2**2*(1+8*p_2*K_2),
                  (1./2)*K_2**2*(1+8*p_2*K_2),
                  (1./2)*K_2**2*(1+8*p_2*(K_1+K_2)),
                  (1./2)*K_2**2*(1+8*p_2*(K_1+K_2)),
                  (1./2)*(2*K_1+K_2)**2*(1+8*p_2*(K_1+K_2)),
                  (1./2)*(2*K_1+K_2)**2*(1+8*p_2*(K_1+K_2)),
                  (1./2)*(2*K_1+K_2)*(16*p_2*K_1**2+(2*K_1+K_2)*(1+16*p_2*K_2)),
                  0,
                  0,
                  0,
                  0,
                  0,
                  0])

def der2_Cov_n2(p_2, K_1, K_2):
    return array([8*K_2**2*(K_1+K_2),
                  8*K_2**2*(K_1+K_2),
                  4*K_2**3,
                  4*K_2**3,
                  4*K_2**2*(K_1+K_2),
                  4*K_2**2*(K_1+K_2),
                  4*(K_1+K_2)*(2*K_1+K_2)**2,
                  4*(K_1+K_2)*(2*K_1+K_2)**2,
                  8*(K_1+K_2)**2*(2*K_1+K_2),
                  0,
                  0,
                  0,
                  0,
                  0,
                  0])

def Cov_n3(p_3, K_1, K_2):
    return array([(1./6)*p_3*K_2**3*(1+12*p_3*(K_1+K_2)*(1+2*K_1+2*K_2)),
                  (1./6)*p_3*K_2**3*(1+12*p_3*(K_1+K_2)*(1+2*K_1+2*K_2)),
                  (1./6)*p_3*K_2**3*(1+6*p_3*K_2*(1+K_2)),
                  (1./6)*p_3*K_2**3*(1+6*p_3*K_2*(1+K_2)),
                  (1./6)*p_3*K_2**3*(1+6*p_3*(K_1+K_2)*(1+K_1+K_2)),
                  (1./6)*p_3*K_2**3*(1+6*p_3*(K_1+K_2)*(1+K_1+K_2)),
                  (1./6)*p_3*(2*K_1+K_2)**3*(1+6*p_3*(K_1+K_2)*(1+K_1+K_2)),
                  (1./6)*p_3*(2*K_1+K_2)**3*(1+6*p_3*(K_1+K_2)*(1+K_1+K_2)),
                  (1./6)*p_3*(2*K_1+K_2)*((2*K_1+K_2)**2+p_3*(12*(K_1+K_2)**2*(2*K_1+K_2+2*(K_1+K_2)**2))),
                  0,
                  0,
                  0,
                  0,
                  0,
                  0])

def der_Cov_n3(p_3, K_1, K_2):
    return array([(1./6)*K_2**3*(1+24*p_3*(K_1+K_2)*(1+2*K_1+2*K_2)),
                  (1./6)*K_2**3*(1+24*p_3*(K_1+K_2)*(1+2*K_1+2*K_2)),
                  (1./6)*K_2**3*(1+12*p_3*K_2*(1+K_2)),
                  (1./6)*K_2**3*(1+12*p_3*K_2*(1+K_2)),
                  (1./6)*K_2**3*(1+12*p_3*(K_1+K_2)*(1+K_1+K_2)),
                  (1./6)*K_2**3*(1+12*p_3*(K_1+K_2)*(1+K_1+K_2)),
                  (1./6)*(2*K_1+K_2)**3*(1+12*p_3*(K_1+K_2)*(1+K_1+K_2)),
                  (1./6)*(2*K_1+K_2)**3*(1+12*p_3*(K_1+K_2)*(1+K_1+K_2)),
                  (1./6)*(2*K_1+K_2)*((2*K_1+K_2)**2+24*p_3*(K_1+K_2)**2*(2*K_1+K_2+2*(K_1+K_2)**2)),
                  0,
                  0,
                  0,
                  0,
                  0,
                  0])

def der2_Cov_n3(p_3, K_1, K_2):
    return array([4*K_2**3*(K_1+K_2)*(1+2*K_1+2*K_2),
                  4*K_2**3*(K_1+K_2)*(1+2*K_1+2*K_2),
                  2*K_2**4*(1+K_2),
                  2*K_2**4*(1+K_2),
                  2*K_2**3*(K_1+K_2)*(1+K_1+K_2),
                  2*K_2**3*(K_1+K_2)*(1+K_1+K_2),
                  2*(K_1+K_2)*(1+K_1+K_2)*(2*K_1+K_2)**3,
                  2*(K_1+K_2)*(1+K_1+K_2)*(2*K_1+K_2)**3,
                  4*(K_1+K_2)**2*(2*K_1+K_2)*(2*K_1+K_2+2*(K_1+K_2)**2),
                  0,
                  0,
                  0,
                  0,
                  0,
                  0])

def Cov_n1n2(p_1, p_2, K_1, K_2):
    return list(array(Cov_n1(p_1, K_1, K_2)) +
                array(Cov_n2(p_2, K_1, K_2)) +
                [2*p_1*p_2*K_2*(K_1+2*K_2),
                 2*p_1*p_2*K_2*(K_1+2*K_2),
                 3*p_1*p_2*K_2**2,
                 3*p_1*p_2*K_2**2,
                 p_1*p_2*K_2*(2*K_1+3*K_2),
                 p_1*p_2*K_2*(2*K_1+3*K_2),
                 p_1*p_2*(2*K_1+K_2)*(4*K_1+3*K_2),
                 p_1*p_2*(2*K_1+K_2)*(4*K_1+3*K_2),
                 4*p_1*p_2*(2*K_1+K_2)*(K_1+K_2),
                 0,
                 0,
                 0,
                 0,
                 0,
                 0])

def Cov_n2n3(p_2, p_3, K_1, K_2):
    return list(array(Cov_n2(p_2, K_1, K_2)) +
                array(Cov_n3(p_3, K_1, K_2)) +
                [p_2*p_3*K_2**2*(K_1+2*K_2)*(1+4*K_1+4*K_2),
                 p_2*p_3*K_2**2*(K_1+2*K_2)*(1+4*K_1+4*K_2),
                 (3./2)*p_2*p_3*K_2**3*(1+2*K_2),
                 (3./2)*p_2*p_3*K_2**3*(1+2*K_2),
                 (1./2)*p_2*p_3*K_2**2*(1+2*K_1+2*K_2)*(2*K_1+3*K_2),
                 (1./2)*p_2*p_3*K_2**2*(1+2*K_1+2*K_2)*(2*K_1+3*K_2),
                 (1./2)*p_2*p_3*(2*K_1+K_2)**2*(1+2*K_1+2*K_2)*(4*K_1+3*K_2),
                 (1./2)*p_2*p_3*(2*K_1+K_2)**2*(1+2*K_1+2*K_2)*(4*K_1+3*K_2),
                 2*p_2*p_3*(2*K_1+K_2)*(K_1+K_2)*(4*K_1**2+(2*K_1+K_2)*(1+4*K_2)),
                 0,
                 0,
                 0,
                 0,
                 0,
                 0])

def Sigma(Var, Cov, eps, obs):
    return missM_wrap(array([
        [Var[0]*(1+eps), Cov[0], Cov[1], Cov[9], Cov[2], Cov[3]],
        [Cov[0], Var[1]*(1+eps), Cov[8], Cov[6], Cov[10], Cov[5]],
        [Cov[1], Cov[8], Var[2]*(1+eps), Cov[7], Cov[4], Cov[11]],
        [Cov[9], Cov[6], Cov[7], Var[3]*(1+eps), Cov[12], Cov[13]],
        [Cov[2], Cov[10], Cov[4], Cov[12], Var[4]*(1+eps), Cov[14]],
        [Cov[3], Cov[5], Cov[11], Cov[13], Cov[14], Var[5]*(1+eps)]]), obs)

def derp_Sigma(dVar, dCov, eps, obs):
    return missM_wrap(array([
        [dVar[0]*(1+eps), dCov[0], dCov[1], dCov[9], dCov[2], dCov[3]],
        [dCov[0], dVar[1]*(1+eps), dCov[8], dCov[6], dCov[10], dCov[5]],
        [dCov[1], dCov[8], dVar[2]*(1+eps), dCov[7], dCov[4], dCov[11]],
        [dCov[9], dCov[6], dCov[7], dVar[3]*(1+eps), dCov[12], dCov[13]],
        [dCov[2], dCov[10], dCov[4], dCov[12], dVar[4]*(1+eps), dCov[14]],
        [dCov[3], dCov[5], dCov[11], dCov[13], dCov[14], dVar[5]*(1+eps)]]), obs)

def derp2_Sigma(dVar2, dCov2, eps, obs):
    return missM_wrap(array([
        [dVar2[0]*(1+eps), dCov2[0], dCov2[1], dCov2[9], dCov2[2], dCov2[3]],
        [dCov2[0], dVar2[1]*(1+eps), dCov2[8], dCov2[6], dCov2[10], dCov2[5]],
        [dCov2[1], dCov2[8], dVar2[2]*(1+eps), dCov2[7], dCov2[4], dCov2[11]],
        [dCov2[9], dCov2[6], dCov2[7], dVar2[3]*(1+eps), dCov2[12], dCov2[13]],
        [dCov2[2], dCov2[10], dCov2[4], dCov2[12], dVar2[4]*(1+eps), dCov2[14]],
        [dCov2[3], dCov2[5], dCov2[11], dCov2[13], dCov2[14], dVar2[5]*(1+eps)]]), obs)

def dere_Sigma(Var, Cov, eps, obs):
    return missM_wrap(array([
        [Var[0], 0, 0, 0, 0, 0],
        [0, Var[1], 0, 0, 0, 0],
        [0, 0, Var[2], 0, 0, 0],
        [0, 0, 0, Var[3], 0, 0],
        [0, 0, 0, 0, Var[4], 0],
        [0, 0, 0, 0, 0, Var[5]]]), obs)

def dere2_Sigma(Var, Cov, eps, obs):
    return missM_wrap(array([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]), obs)

def derpe_Sigma(dVar, Cov, eps, obs):
    return missM_wrap(array([
        [dVar[0], 0, 0, 0, 0, 0],
        [0, dVar[1], 0, 0, 0, 0],
        [0, 0, dVar[2], 0, 0, 0],
        [0, 0, 0, dVar[3], 0, 0],
        [0, 0, 0, 0, dVar[4], 0],
        [0, 0, 0, 0, 0, dVar[5]]]), obs)


def missM_wrap(mat, obs):
    inds = list()
    for idx, item in enumerate(obs):
        if(item < 0):
            inds.append(idx)

    inds.sort()

    while(len(inds) > 0):
        idx = inds.pop()
        mat = delete(delete(mat, idx, 0), idx, 1)

    return mat

def missV_wrap(vec, obs):
    inds = list()
    for idx, item in enumerate(obs):
        if(item < 0):
            inds.append(idx)

    inds.sort()

    while(len(inds) > 0):
        idx = inds.pop()
        vec = delete(vec, idx, 0)

    return vec

def log_likelihood(v, sdet, sinv):
    LL = ((-1./2)*dot(dot(v, sinv), v) -
          (1./2)*log(sdet) -
          3*log(2*pi))

    return LL

def log_likelihood_n1(x, K_1, K_2, obs):
    p_1 = x[0]
    eps = x[1]

    exp = Ex_n1(p_1, K_1, K_2)
    v   = missV_wrap(obs - exp, obs)
    
    sig = Sigma(Var_n1(p_1, K_1, K_2), Cov_n1(p_1, K_1, K_2), eps, obs)

    try:
        sinv = linalg.inv(sig)
        sdet = linalg.det(sig)
    except:
        return nan

    if(sdet <= 0):
        return nan

    return log_likelihood(v, sdet, sinv)

def log_likelihood_n2(x, K_1, K_2, obs):
    p_2 = x[0]
    eps = 0   # eps removed except from lin

    exp = Ex_n2(p_2, K_1, K_2)
    v   = missV_wrap(obs - exp, obs)
    
    sig = Sigma(Var_n2(p_2, K_1, K_2), Cov_n2(p_2, K_1, K_2), eps, obs)
    try:
        sinv = linalg.inv(sig)
        sdet = linalg.det(sig)
    except:
        return nan

    if(sdet <= 0):
        return nan

    return log_likelihood(v, sdet, sinv)

def log_likelihood_n2_dadd(x, K_1, K_2, obs):
    p_a = x[0]
    p_d = x[1]
    eps = 0  # eps removed except from lin

    exp = Ex_n2_dadd(p_a, p_d, K_1, K_2)
    v   = missV_wrap(obs - exp, obs)
    sig = Sigma(Var_n2_dadd(p_a, p_d, K_1, K_2), Cov_n2_dadd(p_a, p_d, K_1, K_2), eps, obs)
    try:
        sinv = linalg.inv(sig)
        sdet = linalg.det(sig)
    except:
        return nan

    if(sdet <= 0):
        return nan

    return log_likelihood(v, sdet, sinv)

def log_likelihood_n3(x, K_1, K_2, obs):
    p_3 = x[0]
    eps = 0   # eps removed except from lin

    exp = Ex_n3(p_3, K_1, K_2)
    v   = missV_wrap(obs - exp, obs)
    sig = Sigma(Var_n3(p_3, K_1, K_2), Cov_n3(p_3, K_1, K_2), eps, obs)
    try:
        sinv = linalg.inv(sig)
        sdet = linalg.det(sig)
    except:
        return nan

    if(sdet <= 0):
        return nan

    return log_likelihood(v, sdet, sinv)

def log_likelihood_n2n3(x, K_1, K_2, obs):
    p_2 = x[0]
    p_3 = x[1]
    eps = 0  # eps removed except from lin

    exp = Ex_n2n3(p_2, p_3, K_1, K_2)
    v   = missV_wrap(obs - exp, obs)
    sig = Sigma(Var_n2n3(p_2, p_3, K_1, K_2), Cov_n2n3(p_2, p_3, K_1, K_2), eps, obs)
    try:
        sinv = linalg.inv(sig)
        sdet = linalg.det(sig)
    except:
        return nan

    if(sdet <= 0):
        return nan

    return log_likelihood(v, sdet, sinv)

def log_likelihood_n1n2(x, K_1, K_2, obs):
    p_1 = x[0]
    p_2 = x[1]
    eps = 0  # eps removed except from lin

    exp = Ex_n1n2(p_1, p_2, K_1, K_2)
    v   = missV_wrap(obs - exp, obs)
    sig = Sigma(Var_n1n2(p_1, p_2, K_1, K_2), Cov_n1n2(p_1, p_2, K_1, K_2), eps, obs)
    try:
        sinv = linalg.inv(sig)
        sdet = linalg.det(sig)
    except:
        return nan

    if(sdet <= 0):
        return nan
  
    return log_likelihood(v, sdet, sinv)
