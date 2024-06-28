from numpy import array, ones
from numpy.testing import assert_allclose
import slycot


def test_sb02md_example():
    A = array([[0, 1],
               [0, 0]])
    Q = array([[1, 0],
               [0, 2]])
    G = array([[0, 0],
               [0, 1]])
    out = slycot.sb02md(2, A, G, Q, 'C')
    print('--- Example for sb02md ---')
    print('The solution X is')
    print(out[0])
    print('rcond =', out[1])
    assert_allclose([[2., 1.], [1., 2.]], out[0])
    assert_allclose(0.30901699437494745, out[1])


if __name__ == "__main__":
    test_sb02md_example()
