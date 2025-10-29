def get_factors(to_factor):
    # x**(0.5) is the square root of x

    # We want to loop until we get to the square root of to_factor
    # Stop is the square root of the factor.
    # Basically instead of going from one to the number
    # we go from 1 to 'stop' (which is the square root
    # of the number we are trying to factorise)

    factors_list = []

    # square root the number to work out when to stop looping
    stop = to_factor ** 0.5
    stop = int(stop)


    for item in range(1, stop + 1):

        #if modulo is zero, then the number is a factor
        if to_factor % item == 0:
            # Add first factor to list
            factors_list.append (item)

        #find second factor by dividing 'to factor' by the first factor
        partner = to_factor // item

        # check second factor is not in list and add it
        if partner not in factors_list:
            factors_list.append(partner)

    #output
    factors_list.sort()
    return factors_list