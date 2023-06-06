class _2x2_matrix:
    def __init__(this, a, b, c, d):
        this._11 = a
        this._12 = b
        this._21 = c
        this._22 = d

    def print(this):
        print ('[' + str(this._11) + ' ' + str(this._12) + ']')
        print ('[' + str(this._21) + ' ' + str(this._22) + "]\n")

def determinant(matrix): return (matrix._11 * matrix._22) - (matrix._12 * matrix._21)

def zero() -> _2x2_matrix: return (_2x2_matrix(0, 0, 0, 0))
def identity() -> _2x2_matrix: return (_2x2_matrix(1, 0, 0, 1))

def add(mtx1, mtx2) -> _2x2_matrix: 
    return _2x2_matrix(
        mtx1._11 + mtx2._11, mtx1._12 + mtx2._12, 
        mtx1._21 + mtx2._21, mtx1._22 + mtx2._22
    )

def subtract(mtx1, mtx2) -> _2x2_matrix:
    return _2x2_matrix(
        mtx1._11 - mtx2._11, mtx1._12 - mtx2._12, 
        mtx1._21 - mtx2._21, mtx1._22 - mtx2._22
    )

def multiply_by_scalar(mtx1, scalar) -> _2x2_matrix:
    return _2x2_matrix(
        scalar * mtx1._11, scalar * mtx1._12,
        scalar * mtx1._21, scalar * mtx1._22
    )

def multiply_by_matrix(mtx1, mtx2) -> _2x2_matrix:
    return _2x2_matrix(
        mtx1._11 * mtx2._11 + mtx1._12 * mtx2._21, mtx1._11 * mtx2._12 + mtx1._12 * mtx2._22,
        mtx1._21 * mtx2._11 + mtx1._22 * mtx2._21, mtx1._21 * mtx2._12 + mtx1._22 * mtx2._22
    )

def inverse(matrix) -> _2x2_matrix:
    output : _2x2_matrix
    
    try:
        output = _2x2_matrix(
            (1/determinant(matrix)) * matrix._22, (1/determinant(matrix)) * -matrix._12, 
            (1/determinant(matrix)) * -matrix._21, (1/determinant(matrix)) * matrix._11
        )
    except:
        output = identity

    return output