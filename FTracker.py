from mathutils import Matrix, Vector


class FTracker:
    def __init__(self, tracker):
        self.tracker = tracker
        self.m_start = None

    def init(self):
        self.m_start = self.tracker.matrix_world.copy()

    # Get plain matrix
    def get_matrix(self) -> Matrix:
        return self.tracker.matrix_world * self.m_start.inverted()

    # Get translation matrix
    def get_translation_matrix(self, v_factor: Vector = Vector((1, 1, 1))) -> Matrix:
        v_translation = self.get_matrix().to_translation()
        return Matrix.Translation((
            v_translation.x * v_factor.x,
            v_translation.y * v_factor.y,
            v_translation.z * v_factor.z
        ))

