from mathutils import Matrix, Vector


class FBoundaries:
    def __init__(self, v_max1: Vector, v_max2: Vector):
        self.v_max1 = v_max1
        self.v_max2 = v_max2

    # Fix matrix by boundaries
    def fix(self, m_matrix):
        v_translation = m_matrix.to_translation()

        v_translation.x = self.fix_axis(v_translation, 0)
        v_translation.y = self.fix_axis(v_translation, 1)
        v_translation.z = self.fix_axis(v_translation, 2)

        return Matrix.Translation(v_translation)

    def fix_axis(self, v_location: Vector, s_axis: int):
        i_max1 = self.v_max1[s_axis]
        i_max2 = self.v_max2[s_axis]

        i_axis = v_location[s_axis]
        i_min = i_max1 if i_max1 < i_max2 else i_max2
        i_max = i_max1 if i_max1 > i_max2 else i_max2

        if i_axis > i_max:
            return i_max
        elif i_axis < i_min:
            return i_min
        else:
            return i_axis
