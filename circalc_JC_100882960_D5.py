#""" circalc.py -- simplistic LCR calculator for TPRG 2131 Week 3 Asmt 5

#Assignment 5 for Tprg 2131 intro week 1-2

# Jhyg Castillejos (100882960)
# TPRG1131 Section 2131
# september 18, 2023
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s).
# The program calculates the resonant frequency, bandwidth and Q factor based
# on the inductance, capacitance and reesistance inputed by the user.
#Bandwidth formula for series circuit- Bandwidth - https://byjusexamprep.com/bandwidth-formula-rlc-circuit-i#:~:text=The%20bandwidth%20formula%20for%20the,is%20B.W%3DR%2FL.&text=The%20bandwidth%20of%20the%20rlc,occur%20at%20the%20resonant%20frequency.
#Q Factor formula for series circuit-  https://www.omnicalculator.com/physics/rlc-circuit#:~:text=Measure%20the%20resistance%20of%20the,%E2%88%9A(L%2FC)%20.
#total resistor formula(parallel)- https://phys.libretexts.org/Bookshelves/College_Physics/College_Physics_1e_(OpenStax)/21%3A_Circuits_Bioelectricity_and_DC_Instruments/21.01%3A_Resistors_in_Series_and_Parallel

#READY FOR MARKING

#-------------------------------------------------------------------------------

#imports pi and square root function
from math import pi
from math import sqrt

print("Series resonant circuit calculator\n([q] or [Q] to quit)")


def resonant_frequency(l,c,r):
    freq=1/(2*pi*(sqrt((l/1000)*(c/1000000))))
    return (round(freq,2))
#Define functions under this comment calculates the
#bandwidth, and the Q factor for a series circuit when called.
def bandwidth(l,c,r):
    freq=1/(2*pi*(sqrt((l/1000)*(c/1000000))))
    q_fact= (1/r*sqrt((l/1000)/(c/1000000)))
    bandwidth=freq/q_fact
    return (round(bandwidth,2))

def quality_factor(l,c,r):
    q_fact= (1/r*sqrt((l/1000)/(c/1000000)))
    return (round(q_fact,2))

#Define function under this comment calculates the total resistance for parallel circuit.
def total_resistance(r1,r2):
    total_res=(1/r1)+(1/r2)
    total_res= 1/total_res
    return round(total_res,2)

#Define function under this comment calculates the rc time constant of parallel circuit.
def Time_constant(r,c):
    return round((r*(c/1000000)),2)

#calculates bandwidth for series rlc circuit
def bandwidth2(l,c,r):
    bandwidth=r/(l/1000)
    return (round(bandwidth,2))



while True:
    #asks user if the circuit is series or parallel.
    option=input("Type of circuit? [series] or [parallel]: ")
    
#if user enters "q or "Q", code quits.
    if option == "q":
        exit()
    elif option == "Q":
        exit()
    elif option == "series":
        #if the number inputed by the user is equal to or less than zero,
        #the define function prompts the user to write a number greater than zero
        def check(user_in):
            return float(input("The value must be greater than zero\n"
                                "What is the inductance in mH? "))
        def check2(user_in):
            return float(input("The value must be greater than zero\n"
                                    "What is the capacitance in uF? "))
        def check3(user_in):
            return float(input("The value must be greater than zero\n"
                                    "What is the resistance in ohms? "))

        #asks the user to input the inductance, capacitance and resistance, if the
        # number is a zero, it calls for the "check" functions above this comment.
        inductance = float(input("What is the inductance in mH? "))
        if inductance <= 0.0:
            inductance = check(inductance)

        capacitance = float(input("What is the capacitance in uF? "))
        if capacitance  <= 0.0:
            capacitance = check2(capacitance)

        resistance = float(input("What is the resistance in ohms? "))
        if resistance  <= 0.0:
            resisitance = check3(resistance)
            
        option3 = input("[series resonant circuit] or [series RLC circuit]: ")
        if option3 == "series resonant circuit": 
            # prints the inductance, capacitance, resistance, resonant frequency, 
            # bandwidth and Q factor values of series circuit.
            print("\nlcr:", inductance, capacitance, resistance, "\n")
            print("resonant frequency:", resonant_frequency
                (inductance, capacitance, resistance), "hz\n")
            print("bandwidth:", bandwidth
                    (inductance, capacitance, resistance), "hz\n")
                    
            print("Q factor:", quality_factor
                    (inductance, capacitance, resistance), "\n")
        else:
            print("resonant frequency of RLC circuit:", resonant_frequency
                (inductance, capacitance, resistance), "hz\n")
            print("bandwidth:", bandwidth2
                    (inductance, capacitance, resistance), "hz\n")
            print("Q factor:", quality_factor
                    (inductance, capacitance, resistance), "\n")
            
    elif option == "parallel":
        option2 = input("type of calculation for parallel? [total resistance] or [rc time constant]: ")
        if option2 == "total resistance":
            def check3(user_in):
                return float(input("The value must be greater than zero\n"
                                    "What is the resistance in ohms? "))
            #asks user for resistor values
            resistance_1 = float(input("What is the resistance of resistor 1 in ohms? "))
            if resistance_1  <= 0.0:
                resistance = check3(resistance)
            resistance_2 = float(input("What is the resistance of resistor 2 in ohms? "))
            if resistance_2  <= 0.0:
                resistance = check3(resistance)
                
            # prints the total resistance value of parallel circuit.
            print("total resistance:", total_resistance
                (resistance_1, resistance_2), "ohms\n")
            
        elif option2 == "rc time constant":
           #asks user for value of resistor and capacitor to calculate time constant
            resistance_rc = float(input("What is the resistance of resistor in ohms? "))
            capacitance_rc = float(input("What is the capacitance of capacitor in uF? "))
            
            print("RC time constant:", Time_constant(resistance_rc, capacitance_rc ), "seconds\n")
        else:
            print ("choice is not available or typing is incorrect, please try again.")
    else:
         print ("choice is not available or typing is incorrect, please try again.")
        
