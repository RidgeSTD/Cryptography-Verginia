__author__ = 'alex'
import distribution_training


dis = {}


def main():
    global dis
    dis = distribution_training.train()
    


if __name__ == '__main__':
    main()