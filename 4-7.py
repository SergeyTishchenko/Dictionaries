def solar_system():
    return {'Mercury': 57.9,
            'Venus': 67.2,
            'Earth': 149.6,
            'Mars': 227.9,
            'Jupiter': 778.3,
            'Saturn': 1427.0,
            'Uranus': 2871.0,
            'Neptune': 4497.1,
            }


if __name__ == '__main__':
    dic = solar_system()
    for i, j in dic.items():
        print "Planet {0} is located at {1} million kilometers from the sun".format(i, j)