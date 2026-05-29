"""PyQt main window for MagicSquare."""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QComboBox,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from boundary.constants import GRID_SIZE
from boundary.schemas import ErrorResponse
from boundary.screen.presenter import (
    ScreenPresenter,
    SolveSuccess,
    ValidationSuccess,
)
from boundary.screen.sample_grids import SAMPLE_GRIDS

_CELL_MIN = 0
_CELL_MAX = 16
_STATUS_STYLE_OK = "color: #1b7f3a; font-weight: bold;"
_STATUS_STYLE_ERROR = "color: #c0392b; font-weight: bold;"
_STATUS_STYLE_INFO = "color: #2c3e50; font-weight: bold;"
_STATUS_STYLE_PENDING = "color: #7f8c8d; font-weight: bold;"


class MainWindow(QMainWindow):
    """4×4 magic square puzzle viewer and solver shell."""

    def __init__(self, presenter: ScreenPresenter | None = None) -> None:
        super().__init__()
        self._presenter = presenter or ScreenPresenter()
        self._cells: list[list[QSpinBox]] = []
        self._result_cells: list[list[QLabel]] = []
        self._init_ui()

    def _init_ui(self) -> None:
        self.setWindowTitle("MagicSquare — 4×4 마방진")
        self.setMinimumSize(820, 560)

        central = QWidget()
        self.setCentralWidget(central)
        root = QHBoxLayout(central)
        root.setSpacing(16)

        root.addLayout(self._build_input_panel(), stretch=3)
        root.addLayout(self._build_result_panel(), stretch=2)

    def _build_input_panel(self) -> QVBoxLayout:
        layout = QVBoxLayout()

        title = QLabel("입력 격자")
        title.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        layout.addWidget(title)

        hint = QLabel("0 = 빈칸 · 값 범위 0~16")
        hint.setStyleSheet("color: #666;")
        layout.addWidget(hint)

        grid_box = QGroupBox("4 × 4")
        grid_layout = QGridLayout(grid_box)
        grid_layout.setSpacing(6)

        for row in range(GRID_SIZE):
            row_cells: list[QSpinBox] = []
            for col in range(GRID_SIZE):
                spin = QSpinBox()
                spin.setRange(_CELL_MIN, _CELL_MAX)
                spin.setAlignment(Qt.AlignmentFlag.AlignCenter)
                spin.setFont(QFont("Consolas", 14))
                spin.setMinimumSize(56, 44)
                grid_layout.addWidget(spin, row, col)
                row_cells.append(spin)
            self._cells.append(row_cells)

        layout.addWidget(grid_box)

        sample_row = QHBoxLayout()
        sample_row.addWidget(QLabel("샘플:"))
        self._sample_combo = QComboBox()
        self._sample_combo.addItem("— 선택 —", None)
        for name in SAMPLE_GRIDS:
            self._sample_combo.addItem(name, name)
        self._sample_combo.currentIndexChanged.connect(self._on_sample_selected)
        sample_row.addWidget(self._sample_combo, stretch=1)
        layout.addLayout(sample_row)

        btn_row = QHBoxLayout()
        self._validate_btn = QPushButton("크기 검증")
        self._validate_btn.clicked.connect(self._on_validate)
        self._solve_btn = QPushButton("풀이")
        self._solve_btn.clicked.connect(self._on_solve)
        self._clear_btn = QPushButton("초기화")
        self._clear_btn.clicked.connect(self._on_clear)
        btn_row.addWidget(self._validate_btn)
        btn_row.addWidget(self._solve_btn)
        btn_row.addWidget(self._clear_btn)
        layout.addLayout(btn_row)

        scenario_row = QHBoxLayout()
        scenario_row.addWidget(QLabel("크기 검증 시나리오:"))
        self._scenario_combo = QComboBox()
        self._scenario_combo.addItem("현재 격자", "current")
        self._scenario_combo.addItem("null (INVALID_SIZE)", "null")
        self._scenario_combo.addItem("빈 리스트 [] (INVALID_SIZE)", "empty")
        self._scenario_combo.addItem("3×4 (INVALID_SIZE)", "3x4")
        scenario_row.addWidget(self._scenario_combo, stretch=1)
        layout.addLayout(scenario_row)
        layout.addStretch()
        return layout

    def _build_result_panel(self) -> QVBoxLayout:
        layout = QVBoxLayout()

        title = QLabel("작업 결과")
        title.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        layout.addWidget(title)

        self._status_label = QLabel("격자를 입력하고 검증 또는 풀이를 실행하세요.")
        self._status_label.setWordWrap(True)
        self._status_label.setStyleSheet(_STATUS_STYLE_PENDING)
        layout.addWidget(self._status_label)

        detail_box = QGroupBox("상세")
        detail_layout = QVBoxLayout(detail_box)
        self._detail_text = QTextEdit()
        self._detail_text.setReadOnly(True)
        self._detail_text.setFont(QFont("Consolas", 10))
        self._detail_text.setPlaceholderText("오류 코드, 풀이 좌표, 백엔드 메시지가 여기에 표시됩니다.")
        detail_layout.addWidget(self._detail_text)
        layout.addWidget(detail_box)

        result_box = QGroupBox("풀이 후 격자")
        result_grid = QGridLayout(result_box)
        result_grid.setSpacing(4)
        for row in range(GRID_SIZE):
            row_labels: list[QLabel] = []
            for col in range(GRID_SIZE):
                label = QLabel("—")
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                label.setFont(QFont("Consolas", 13))
                label.setFrameShape(QFrame.Shape.Box)
                label.setMinimumSize(48, 40)
                label.setStyleSheet("background: #f8f9fa;")
                result_grid.addWidget(label, row, col)
                row_labels.append(label)
            self._result_cells.append(row_labels)
        layout.addWidget(result_box)
        layout.addStretch()
        return layout

    def read_grid(self) -> list[list[int]]:
        """Read the current 4×4 values from spin boxes."""
        return [
            [self._cells[row][col].value() for col in range(GRID_SIZE)]
            for row in range(GRID_SIZE)
        ]

    def load_grid(self, grid: list[list[int]]) -> None:
        """Populate spin boxes from a grid matrix."""
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                self._cells[row][col].setValue(grid[row][col])

    def _on_sample_selected(self, _index: int) -> None:
        name = self._sample_combo.currentData()
        if name is None:
            return
        self.load_grid(SAMPLE_GRIDS[name])
        self._sample_combo.setCurrentIndex(0)
        self._set_status("샘플 격자를 불러왔습니다.", _STATUS_STYLE_INFO)
        self._detail_text.clear()
        self._clear_result_grid()

    def _on_clear(self) -> None:
        self.load_grid([[0] * GRID_SIZE for _ in range(GRID_SIZE)])
        self._set_status("격자를 초기화했습니다.", _STATUS_STYLE_PENDING)
        self._detail_text.clear()
        self._clear_result_grid()

    def _on_validate(self) -> None:
        grid = self._grid_for_validation_scenario()
        result = self._presenter.validate(grid)
        self._clear_result_grid()

        if isinstance(result, ErrorResponse):
            self._set_status(f"[{result.code}] {result.message}", _STATUS_STYLE_ERROR)
            self._detail_text.setPlainText(
                f"code: {result.code}\nmessage: {result.message}"
            )
            return

        if isinstance(result, ValidationSuccess):
            self._set_status(result.message, _STATUS_STYLE_OK)
            self._detail_text.setPlainText(
                "BoundaryValidator: 크기 검증 통과 (4×4).\n"
                "추가 입력 검증(E002~E005)은 Report/09 GREEN 이후 제공됩니다."
            )

    def _grid_for_validation_scenario(
        self,
    ) -> list[list[int]] | None:
        scenario = self._scenario_combo.currentData()
        if scenario == "null":
            return None
        if scenario == "empty":
            return []
        if scenario == "3x4":
            return [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
            ]
        return self.read_grid()

    def _on_solve(self) -> None:
        grid = self.read_grid()
        result = self._presenter.solve(grid)

        if isinstance(result, ErrorResponse):
            self._set_status(f"[{result.code}] {result.message}", _STATUS_STYLE_ERROR)
            self._detail_text.setPlainText(
                f"code: {result.code}\nmessage: {result.message}"
            )
            self._clear_result_grid()
            return

        if isinstance(result, SolveSuccess):
            solution = result.solution
            self._set_status(
                f"풀이 성공: [{', '.join(str(v) for v in solution)}]",
                _STATUS_STYLE_OK,
            )
            self._detail_text.setPlainText(
                "solution (1-index): "
                f"({solution[0]},{solution[1]})={solution[2]}, "
                f"({solution[3]},{solution[4]})={solution[5]}\n"
                f"full: {solution}"
            )
            self._show_filled_grid(result.filled_grid)

    def _set_status(self, text: str, style: str) -> None:
        self._status_label.setText(text)
        self._status_label.setStyleSheet(style)

    def _clear_result_grid(self) -> None:
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                self._result_cells[row][col].setText("—")
                self._result_cells[row][col].setStyleSheet("background: #f8f9fa;")

    def _show_filled_grid(self, grid: list[list[int]]) -> None:
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                value = grid[row][col]
                label = self._result_cells[row][col]
                label.setText(str(value))
                if value == 0:
                    label.setStyleSheet("background: #fff3cd;")
                else:
                    label.setStyleSheet("background: #d4edda;")
