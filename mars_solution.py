    earth_weight_str = input('Enter a weight on earth: ')

    earth_weight = float(earth_weight_str)

    mars_weight = earth_weight * MARS_MULTIPLE

    print('The equivalent weight on Mars: ' + str(mars_weight))