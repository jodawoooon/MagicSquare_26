# MagicSquare 결함 목록 (Defect List)

| 항목 | 내용 |
|---|---|
| **문서 버전** | 1.0 |
| **작성일** | 2026-05-29 |
| **작성자** | QA Lead |
| **기준 실행** | `python -m pytest tests/boundary tests/control -v --tb=long` |
| **TDD 단계** | RED (의도적 실패 — GREEN 미착수) |
| **관련 AC** | AC-FR-01-01, AC-FR-01-05 (연계) |
| **관련 문서** | `test_plan.md`, `Report/05. MagicSquare_AC_FR_01_01_RED_Test_Implementation_Report.md` |

---

## 실행 요약 (2026-05-29)

| 결과 | 건수 |
|---|---|
| ERROR | 6 |
| FAILED | 2 |
| PASSED | 1 |
| **합계** | 9 |

```text
6 failed, 1 passed, 6 errors  (exit code 1)
```

> **판정**: 실패 원인은 비즈니스 로직 오류가 아니라 **프로덕션 ECB 패키지 미구현**이다. RED 단계 목적(의도한 이유로 실패)에는 부합하나, GREEN 전까지는 AC-FR-01-01 계약 Assert가 **한 건도 실행되지 않음**.

---

## 결함 목록

| ID | Severity | AC ID | 재현 절차 | 기대값 | 실제값 | 근본 원인 | 수정 요약 |
|---|---|---|---|---|---|---|---|
| DEF-001 | **Critical** | AC-FR-01-01 | 1. `grid = None` 준비<br>2. `boundary_validator` fixture로 `BoundaryValidator.validate(grid)` 호출 (`test_none_grid_returns_invalid_size_code_message`) | `{ code: "INVALID_SIZE", message: "Grid must be 4x4." }` | `ModuleNotFoundError: No module named 'boundary'` (fixture setup, `conftest.py:9`) | `boundary` 패키지·`BoundaryValidator` 미구현 | `boundary/__init__.py`, `boundary/validator.py`, `boundary/schemas.py`(`ErrorResponse`) 추가; `validate()`에서 `grid is None` 등 크기 선행 검사 후 표준 오류 반환 |
| DEF-002 | **Critical** | AC-FR-01-01 | 1. `grid = []` 준비<br>2. 동일 fixture로 `validate(grid)` (`test_empty_list_grid_returns_invalid_size_code_message`) | `code="INVALID_SIZE"`, `message="Grid must be 4x4."` | `ModuleNotFoundError: No module named 'boundary'` | DEF-001과 동일 — Boundary 레이어 부재 | DEF-001 수정 후 `len(grid) != 4` 분기로 빈 리스트 거부 |
| DEF-003 | **Critical** | AC-FR-01-01 | 1. `grid = [[]] * 4` 준비<br>2. `validate(grid)` (`test_four_empty_rows_grid_returns_invalid_size_code_message`) | `INVALID_SIZE` 오류 응답 | `ModuleNotFoundError: No module named 'boundary'` | DEF-001과 동일; 열 길이 검사 로직 없음 | DEF-001 수정 후 각 행 `len(row) == 4` 검증 추가 |
| DEF-004 | **Critical** | AC-FR-01-01 | 1. 3×4 행렬 `GRID_3X4` 준비<br>2. `validate(grid)` (`test_3x4_grid_returns_invalid_size_code_message`) | `INVALID_SIZE` 오류 응답 | `ModuleNotFoundError: No module named 'boundary'` | DEF-001과 동일 — 행 수 ≠ 4 미처리 | DEF-001 수정 후 행·열 4×4 불변(BR-01) 검증 |
| DEF-005 | **Major** | AC-FR-01-01 | 1. `grid = None`<br>2. `validate(grid)` 후 `result.message` 비교 (`test_none_grid_message_exact_match_prd_section_8_1_string`) | `message == "Grid must be 4x4."` (UTF-8 바이트 동일) | `ModuleNotFoundError: No module named 'boundary'` | DEF-001과 동일; 메시지 상수·반환 경로 없음 | `INVALID_SIZE_MESSAGE` 상수를 PRD §8.1 문구와 동일하게 정의 후 반환 |
| DEF-006 | **Major** | AC-FR-01-01 | 1. `grid = None`<br>2. `validate(grid)` 반환 타입 검사 (`test_none_grid_returns_error_response_struct_type`) | `isinstance(result, ErrorResponse)` (pydantic) | `ModuleNotFoundError: No module named 'boundary'` (import `boundary.schemas` 전 단계 중단) | `ErrorResponse` 스키마·타입 계약 미정의 | `boundary/schemas.py`에 pydantic `ErrorResponse` 구현; `validate()` 반환 타입 고정 |
| DEF-007 | **Critical** | AC-FR-01-01, AC-FR-01-05 | 1. `grid = None`, `MagicSquareSolver` mock 생성<br>2. `MagicSquareResolver(solver=mock).resolve(grid)` (`test_none_grid_resolve_called_zero_times_spy_mock`) | `result.code/message` = `INVALID_SIZE` 계약; `mock_solver.resolve.call_count == 0` | `ModuleNotFoundError: No module named 'control'` (`test_ac_fr_01_01_domain_isolation.py:17`) | `control` 패키지·`MagicSquareResolver` 미구현 | `control/resolver.py` 추가; 크기 검증 실패 시 Boundary/Control 조기 반환, `solver.resolve` 미호출 |
| DEF-008 | **Critical** | AC-FR-01-01, AC-FR-01-05 | 1. `grid = None`, mock에 `resolve.return_value = [1..6]` 설정<br>2. `resolver.resolve(grid)` (`test_none_grid_resolve_mock_invocation_fails_test_guard`) | Domain 미호출 + `INVALID_SIZE` 응답; 성공 배열 반환 시 AssertionError | `ModuleNotFoundError: No module named 'control'` | DEF-007과 동일 | DEF-007 수정; 입력 오류 시 Domain 성공 결과로 오염되지 않도록 guard 유지 |
| DEF-009 | **Major** | AC-FR-01-05 | DEF-007·008 수정 후 `from entity.solver import MagicSquareSolver` 경로 실행 | `MagicSquareSolver` import 및 mock autospec 성공 | (잠재) `ModuleNotFoundError: No module named 'entity.solver'` — 현재는 `control`에서 선행 차단 | `entity/solver.py` 스텁 미존재 (`entity/user.py`만 존재) | `entity/solver.py`에 `MagicSquareSolver.resolve()` 스텁 추가 (GREEN 최소 구현) |
| DEF-010 | **Minor** | AC-FR-01-01 | pytest 전체 스위트 실행 후 커버리지 측정 (`pytest --cov=boundary --cov=control`) | Boundary ≥85%, Control ≥85% | 측정 대상 모듈 없음 — 커버리지 0% / 측정 불가 | 프로덕션 소스 부재 | DEF-001~009 해소 후 pytest-cov 재측정 |

---

## 심각도 정의

| Severity | 기준 |
|---|---|
| **Critical** | AC-FR-01-01 핵심 계약(크기 검증·Domain 미호출) 테스트 실행 불가 |
| **Major** | 동일 AC 내 부가 계약(메시지·타입·의존 스텁) 미검증 |
| **Minor** | 품질 게이트(커버리지) 미충족 — 기능 차단은 아님 |

---

## 상태 및 GREEN 수정 순서

| 순서 | ID | 상태 | GREEN 완료 조건 |
|---|---|---|---|
| 1 | DEF-001 | **Open** | Boundary 6 ERROR → 0 |
| 2 | DEF-006 | **Open** | `ErrorResponse` 타입 테스트 PASS |
| 3 | DEF-005 | **Open** | 메시지 동일성 테스트 PASS |
| 4 | DEF-007, DEF-008 | **Open** | Control 2 FAILED → 0 |
| 5 | DEF-009 | **Open** | `MagicSquareSolver` import 성공 |
| 6 | DEF-010 | **Open** | Boundary/Control 커버리지 목표 달성 |
| — | DEF-002~004 | **Open** | DEF-001 해소 시 동시 해소 예상 |

**회귀 확인 명령** (모든 결함 수정 후):

```bash
python -m pytest tests/boundary tests/control -v
```

---

## 미결함 / 범위 외

| 항목 | 비고 |
|---|---|
| AC-FR-01-02 ~ 05 | 본 RED 커밋 범위 외 — 별도 defect 등록 예정 |
| FR-02 ~ 05 | 본 스위트 미포함 (`test_scope_excludes_...` PASSED로 범위만 확인) |
| PRD `INVALID_MATRIX_SIZE` vs 테스트 `INVALID_SIZE` | 문서·계약 정합성 검토 필요 (결함 등록 보류, GREEN 시 팀 합의) |

---

## 변경 이력

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| 1.0 | 2026-05-29 | RED 단계 pytest 실패 8건 + 잠재 2건 최초 등록 |
