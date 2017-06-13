from mathutils import Matrix


class FUtil:
    # Get global translation matrix
    @staticmethod
    def get_global_translation(m_initial_matrix: Matrix, m_translation: Matrix):
        m_rotation = m_initial_matrix.to_quaternion().to_matrix().to_4x4()
        return m_initial_matrix * (m_rotation.inverted() * m_translation * m_rotation)