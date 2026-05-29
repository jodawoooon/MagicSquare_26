# PRD — Magic Square 4x4 TDD Practice

## 1. Executive Summary
본 프로젝트의 1차 목표는 “정답 마방진 생성”이 아니라, **4x4 마방진 문제를 불변식과 계약 중심으로 검증 가능한 형태로 고정**하는 것이다. 본 PRD는 입력/출력 계약, Domain 불변식, Boundary 책임, Dual-Track TDD(Track A: Boundary/UI Contract, Track B: Domain/Logic Invariant), RED-GREEN-REFACTOR 실행 기준, 그리고 Concept → Rule → Use Case → Contract → Test → Component 추적성을 명시한다.

## 2. Background
문제 배경은 “퍼즐 풀이”가 아니라 “팀이 동일한 판정 기준으로 같은 결론에 도달할 수 있는가”이다. 기존 학습/구현 과정에서 규칙이 구두로만 공유되면, 동일 입력에 대해 서로 다른 결과가 발생하고 회귀 검증이 불가능해진다. 따라서 본 프로젝트는 구현 이전에 규칙과 계약을 고정하고, 테스트 가능 문장으로 요구사항을 확정하는 것을 우선한다.

## 3. Problem Statement
본 문제는 “마방진을 만든다”가 아니라, 다음을 만족하는 **검증 가능한 불변 조건 세트**를 완성하는 것이다.

- 입력은 4x4 정수 행렬이며 빈칸(`0`)은 정확히 2개여야 한다.
- 비어있지 않은 값은 `1~16` 범위이며 중복이 없어야 한다.
- 누락 숫자 2개를 두 빈칸에 정책 순서로 배치했을 때 마방진 상수 `34`를 만족하는 조합을 찾아야 한다.
- 출력은 고정 형식 `int[6] = [r1,c1,n1,r2,c2,n2]`이어야 한다.

입출력 계약이 핵심인 이유는, 계약이 고정되지 않으면 테스트 오라클이 고정되지 않고, 리팩토링 이후 행동 보존 여부를 검증할 수 없기 때문이다.

## 4. Why Now / Why Chain
지금 이 프로젝트를 수행하는 이유는 학습자와 리뷰어가 반복적으로 겪는 다음 문제를 즉시 차단하기 위해서다.

- 구현을 먼저 시작해 요구사항이 뒤늦게 바뀌는 문제
- 테스트 기준이 불명확해 RED 단계가 형식적으로 끝나는 문제
- Boundary와 Domain 책임이 섞여 오류 원인 분리가 불가능한 문제
- 리팩토링 후 계약이 깨져도 탐지되지 않는 문제

Why Chain은 다음으로 고정한다.

- 왜 지금: 구현 전 계약 고정 없이는 이후 모든 테스트가 불안정해진다.
- 왜 프로그램: 동일 입력/동일 출력의 재현성과 회귀 검증 자동화가 필요하다.
- 왜 TDD: 불변식과 계약을 실패 테스트로 먼저 고정해야 의도 보존 리팩토링이 가능하다.

## 5. Target Users
- TDD 학습자
- 코드 리뷰어
- Clean Architecture/ECB 계층 분리 훈련 개발자

사용 환경은 콘솔 실행 또는 테스트 실행 중심이며, UI/DB/Web은 1차 범위에 포함하지 않는다.

## 6. Vision & Epic Goal
**Epic Goal:** 불변식 기반 사고 훈련 시스템 구축

비전은 다음으로 정의한다.

- 정답 하드코딩이 아니라 규칙 기반 검증 습관을 형성한다.
- Boundary 계약과 Domain 규칙을 분리해 변경 영향 범위를 축소한다.
- Dual-Track TDD로 기능 추가보다 계약 보존을 우선한다.
- 요구사항-검증-컴포넌트를 추적 가능하게 유지한다.

## 7. Persona
- TDD를 학습 중이며 RED 단계에서 무엇을 실패시켜야 하는지 자주 혼동하는 개발자
- ECB 계층 분리를 이해하려는 개발자
- 알고리즘 정답 자체보다 설계-계약-테스트-리팩토링 흐름 훈련을 목표로 하는 사용자

## 8. User Journey Summary
- 문제 인식: “정답 찾기”가 아닌 “검증 기준 고정”이 목적임을 인식
- 계약 정의: 입력/출력 형식과 실패 코드를 먼저 확정
- 도메인 분리: 빈칸 탐색/누락 숫자 탐색/마방진 판정을 Domain 책임으로 분리
- Dual-Track TDD 진행: Track A와 Track B의 RED를 독립적으로 수행
- 회귀 보호: 리팩토링 후 계약 테스트와 불변 테스트를 동시에 통과

Pain Point와 Learning Outcome:

- Pain: 요구 문장이 추상적임 → Outcome: 측정 가능한 Acceptance Criteria 작성
- Pain: 계층 책임 혼재 → Outcome: Boundary 호출 차단 테스트로 경계 고정
- Pain: 리팩토링 후 동작 변형 → Outcome: 계약 테스트와 불변 테스트 동시 회귀

## 9. Scope

### 9.1 In-Scope
- 빈칸 좌표 탐색
- 누락 숫자 탐색
- 마방진 판정
- 두 조합 시도 후 결과 반환
- Boundary 입력 검증
- 출력 계약 검증
- RED-GREEN-REFACTOR 흐름에서 테스트 가능한 요구 정의

### 9.2 Out-of-Scope
- UI 화면 개발
- DB 저장/검색
- Web/API 서버 개발
- N×N 일반화
- 완전한 마방진 생성 알고리즘
- 사용자 인증/권한
- 네트워크 오류 처리
- QR 스캔
- 외부 서비스 연동

## 10. Functional Requirements

### FR-01 Input Verification
- Description: 요청 입력이 고정 계약(4x4, 값 범위, 빈칸 개수, 중복 금지)을 만족하는지 검증한다.
- Layer: Boundary
- Input: `int[][] matrix`
- Processing Rules:
  - 4x4 크기 검사
  - 값이 `0` 또는 `1~16`인지 검사
  - `0` 개수가 정확히 2인지 검사
  - `0` 제외 중복 값 존재 여부 검사
- Output:
  - 성공: 검증 통과 상태
  - 실패: 표준 오류 응답
- Acceptance Criteria:
  - AC-FR01-01: 4x4가 아니면 `INVALID_MATRIX_SIZE`
  - AC-FR01-02: 빈칸 수가 2가 아니면 `INVALID_BLANK_COUNT`
  - AC-FR01-03: 범위 외 값이 있으면 `VALUE_OUT_OF_RANGE`
  - AC-FR01-04: `0` 제외 중복이 있으면 `DUPLICATE_NON_ZERO_VALUE`
  - AC-FR01-05: FR-01 실패 시 Domain resolver를 호출하지 않는다.
- Error / Exception Policy: 오류 응답 반환 방식 사용
- Related Business Rules: BR-01, BR-02, BR-03, BR-04
- Related Test Direction: Track A 입력 검증 실패 케이스
- Component Candidate: `BoundaryValidator`

### FR-02 Blank Coordinate Discovery
- Description: row-major 기준으로 빈칸 두 좌표를 탐색한다.
- Layer: Domain
- Input: 검증 완료 4x4 행렬
- Processing Rules:
  - 행 우선 스캔으로 `0` 위치 2개를 수집
  - 첫 번째 발견 좌표를 first blank로 고정
- Output: 빈칸 좌표 2개(내부 좌표 모델)
- Acceptance Criteria:
  - AC-FR02-01: 빈칸은 정확히 2개가 도출된다.
  - AC-FR02-02: 첫 번째 빈칸은 row-major 첫 발견 `0`이다.
- Error / Exception Policy: FR-01이 선행 차단하므로 본 단계에서 입력 오류를 재검증하지 않는다.
- Related Business Rules: BR-05
- Related Test Direction: Track B row-major 순서 케이스
- Component Candidate: `BlankFinder`

### FR-03 Missing Number Discovery
- Description: 누락 숫자 2개를 도출하고 오름차순으로 고정한다.
- Layer: Domain
- Input: 검증 완료 4x4 행렬
- Processing Rules:
  - `1~16` 중 행렬에 없는 값 2개 추출
  - `(small, large)` 오름차순 정렬
- Output: `nSmall, nLarge`
- Acceptance Criteria:
  - AC-FR03-01: 누락 숫자는 정확히 2개다.
  - AC-FR03-02: 반환 순서는 항상 오름차순이다.
- Error / Exception Policy: FR-01 선행
- Related Business Rules: BR-06, BR-07
- Related Test Direction: Track B 누락 숫자/정렬 케이스
- Component Candidate: `MissingNumberFinder`

### FR-04 Magic Square Validation
- Description: 완성 후보 행렬이 마방진 조건을 만족하는지 판정한다.
- Layer: Domain
- Input: 두 빈칸이 채워진 4x4 후보 행렬
- Processing Rules:
  - 4개 행 합, 4개 열 합, 2개 대각선 합이 모두 34인지 검사
- Output: `true/false`
- Acceptance Criteria:
  - AC-FR04-01: 행/열/대각선 합이 모두 34면 `true`
  - AC-FR04-02: 하나라도 34가 아니면 `false`
- Error / Exception Policy: 판정 결과는 불리언으로 반환한다.
- Related Business Rules: BR-08, BR-09
- Related Test Direction: Track B validator 정상/실패 케이스
- Component Candidate: `MagicSquareValidator`

### FR-05 Two-Combination Solver and Result Formatting
- Description: 두 조합을 순서대로 시도해 성공 조합을 `int[6]` 형식으로 반환한다.
- Layer: Control + Domain + Boundary Output Contract
- Input: 검증 완료 4x4 행렬
- Processing Rules:
  - Attempt 1: small→first blank, large→second blank
  - Attempt 2: Attempt 1 실패 시 reverse
  - 둘 다 실패하면 고정 실패 정책 반환
  - 성공 시 좌표는 1-index로 반환
- Output:
  - 성공: `[r1,c1,n1,r2,c2,n2]`
  - 실패: `NO_VALID_ASSIGNMENT`
- Acceptance Criteria:
  - AC-FR05-01: small-first 성공 시 해당 순서 반환
  - AC-FR05-02: small-first 실패 + reverse 성공 시 reverse 순서 반환
  - AC-FR05-03: 두 조합 모두 실패 시 `NO_VALID_ASSIGNMENT`
  - AC-FR05-04: 성공 출력 길이는 6이고 좌표는 1~4 범위다.
- Error / Exception Policy: 실패는 표준 오류 응답 코드로 반환한다.
- Related Business Rules: BR-10, BR-11, BR-12, BR-13
- Related Test Direction: Track B solver 3경로 + Track A 출력 계약
- Component Candidate: `Solver`, `ResultFormatter`

## 11. Business Rules / Domain Rules

- BR-01: 입력 행렬은 항상 4행 4열이어야 한다.
- BR-02: 입력에서 빈칸 값 `0`은 항상 정확히 2개여야 한다.
- BR-03: 각 셀 값은 항상 `0` 또는 `1~16`이어야 한다.
- BR-04: `0`을 제외한 숫자는 항상 중복될 수 없다.
- BR-05: 첫 번째 빈칸은 항상 row-major 스캔에서 처음 발견되는 `0`이다.
- BR-06: 누락 숫자는 항상 정확히 2개다.
- BR-07: 누락 숫자 쌍은 항상 오름차순 `(small, large)`로 정의한다.
- BR-08: 4x4 마방진 상수는 항상 `34`다.
- BR-09: 완성 후보의 4개 행, 4개 열, 2개 대각선 합은 항상 34여야 마방진이다.
- BR-10: Solver는 항상 Attempt 1(small-first)을 먼저 평가한다.
- BR-11: Attempt 1 실패 시에만 Attempt 2(reverse)를 평가한다.
- BR-12: 성공 출력 좌표는 항상 1-index 규칙을 따른다.
- BR-13: 성공 출력은 항상 `int[6]=[r1,c1,n1,r2,c2,n2]` 형식이다.

## 12. Input / Output Contract

### 12.1 Input Contract

| Field / Item | Type | Rule | Valid Example | Invalid Example | Related Error Code 또는 Failure Policy |
|---|---|---|---|---|---|
| matrix | `int[4][4]` | 크기는 정확히 4x4 | `[[16,0,3,13],[5,11,10,8],[9,7,6,12],[4,14,0,1]]` | `[[1,2,3],[4,5,6]]` | `INVALID_MATRIX_SIZE` |
| matrix value | `int` | 값은 `0` 또는 `1..16` | `0`, `1`, `16` | `-1`, `17` | `VALUE_OUT_OF_RANGE` |
| blank count | `int` | `0` 개수는 정확히 2 | `0`이 2개 | `0`이 1개/3개 | `INVALID_BLANK_COUNT` |
| uniqueness | rule | `0` 제외 값 중복 금지 | `1..16` 중복 없음 | `5`가 두 번 | `DUPLICATE_NON_ZERO_VALUE` |

### 12.2 Output Contract

| Field / Item | Type | Rule | Valid Example | Invalid Example | Related Error Code 또는 Failure Policy |
|---|---|---|---|---|---|
| success result | `int[6]` | 길이 6, 형식 `[r1,c1,n1,r2,c2,n2]` | `[1,2,2,1,3,3]` | 길이 5 또는 순서 불일치 | 계약 위반(내부 오류) |
| coordinates | `int` | `r1,c1,r2,c2`는 1-index(1~4) | `1,4` | `0,5` | 계약 위반(내부 오류) |
| numbers | `int` | `n1,n2`는 누락 숫자 집합과 동일 | `2,3` | `2,17` | 계약 위반(내부 오류) |
| failure response | object | 표준 오류 코드/메시지 반환 | `{code:"NO_VALID_ASSIGNMENT",message:"..."}` | 코드 누락 | 고정 실패 응답 정책 |

## 13. Error / Failure Policy

| Error Code | Message | Layer | Domain resolver 호출 여부 | Related Acceptance Criteria |
|---|---|---|---|---|
| INVALID_MATRIX_SIZE | 입력은 4x4 정수 행렬이어야 한다. | Boundary | No | AC-FR01-01, AC-FR01-05 |
| INVALID_BLANK_COUNT | 빈칸(0)은 정확히 2개여야 한다. | Boundary | No | AC-FR01-02, AC-FR01-05 |
| VALUE_OUT_OF_RANGE | 값은 0 또는 1~16만 허용된다. | Boundary | No | AC-FR01-03, AC-FR01-05 |
| DUPLICATE_NON_ZERO_VALUE | 0을 제외한 숫자는 중복될 수 없다. | Boundary | No | AC-FR01-04, AC-FR01-05 |
| NO_VALID_ASSIGNMENT | 두 조합 모두 마방진 조건을 만족하지 않는다. | Domain → Boundary 매핑 | Yes(이미 호출됨) | AC-FR05-03 |

고정 정책:
- 입력 검증 실패(상위 4개)는 **항상 Boundary에서 종료**한다.
- 두 조합 실패는 **항상 `NO_VALID_ASSIGNMENT` 오류 응답**으로 반환한다.
- 본 PRD는 실패 시 예외 throw 대신 **표준 오류 응답 반환 정책**을 채택한다.

## 14. Non-Functional Requirements
- NFR-01 Coverage: Domain Logic 테스트 커버리지는 95% 이상이어야 한다.
- NFR-02 Coverage: Boundary Validation 테스트 커버리지는 85% 이상이어야 한다.
- NFR-03 Deterministic execution: 동일 입력은 항상 동일 출력(성공 배열 또는 동일 오류 코드)을 반환해야 한다.
- NFR-04 No side effects: 입력 행렬은 처리 전후 값과 구조가 변경되지 않아야 한다.
- NFR-05 Performance: 4x4 단일 실행은 50ms 이내여야 한다.
- NFR-06 Maintainability: Boundary/Control/Entity 책임을 분리해야 한다.
- NFR-07 Maintainability: 설명 없는 매직 넘버 사용을 금지하고 명명된 상수를 사용해야 한다.

## 15. Dual-Track TDD Strategy

### 15.1 Track A — Boundary / UI Contract TDD
- 입력 검증 실패 코드 테스트
- 성공 출력 형식(`int[6]`, 1-index, 길이 6) 테스트
- 실패 응답 스키마 테스트
- 입력 오류 시 Domain resolver 미호출 테스트

### 15.2 Track B — Domain / Logic TDD
- 빈칸 탐색(row-major first blank) 테스트
- 누락 숫자 탐색 및 오름차순 테스트
- 마방진 판정(행/열/대각선=34) 테스트
- small-first 성공 테스트
- small-first 실패 후 reverse 성공 테스트
- 두 조합 모두 실패 테스트

### 15.3 Parallel Progression Rules
- Track A RED와 Track B RED를 분리한다.
- Track A GREEN과 Track B GREEN은 각각 최소 구현만 허용한다.
- 구조 개선은 REFACTOR 단계에서만 수행한다.
- Domain 전부 구현 후 Boundary를 나중에 붙이는 순차 전략을 금지한다.
- 테스트 약화/삭제로 통과시키는 행위를 금지한다.

## 16. Test Plan / QA

### 16.1 Normal Scenarios
- TC-NOR-001: small-first 성공
- TC-NOR-002: small-first 실패 후 reverse 성공

### 16.2 Exception Scenarios
- TC-EXC-001: 4x4가 아닌 입력
- TC-EXC-002: 빈칸 개수 오류
- TC-EXC-003: 값 범위 오류
- TC-EXC-004: 중복 숫자 오류
- TC-EXC-005: 두 조합 모두 실패

### 16.3 Boundary Scenarios
- TC-BND-001: 최소값 1 검증
- TC-BND-002: 최대값 16 검증
- TC-BND-003: `0`은 빈칸 의미로만 처리
- TC-BND-004: 출력 좌표 1-index 검증
- TC-BND-005: 반환 배열 길이 6 검증

### 16.4 Representative Test Data
- small-first 성공 행렬  
  `[[16,0,0,13],[5,11,10,8],[9,7,6,12],[4,14,15,1]]`
- reverse 성공 행렬  
  `[[16,2,3,13],[5,11,10,8],[9,0,0,12],[4,14,15,1]]`
- invalid size 행렬  
  `[[1,2,3],[4,5,6],[7,8,9]]`
- invalid blank count 행렬(빈칸 1개)  
  `[[16,2,3,13],[5,11,10,8],[9,7,6,12],[4,14,0,1]]`
- duplicate value 행렬  
  `[[16,2,3,13],[5,11,10,8],[9,7,7,12],[4,14,0,0]]`
- invalid range 행렬  
  `[[16,2,3,13],[5,11,10,8],[9,0,17,12],[4,14,0,1]]`

## 17. Architecture Overview, High-Level
- Boundary Layer:
  - 입력 검증 수행
  - 오류 응답 생성
  - 성공 결과 형식 검증 및 반환
- Domain Layer:
  - 빈칸 탐색
  - 누락 숫자 도출
  - 마방진 판정
  - 두 조합 시도 정책 적용
- Control/Application Layer:
  - Boundary와 Domain의 흐름 조정
  - 필요 시 조합 순서 및 오류 전파를 관리

의존 방향:
- `Boundary -> Control -> Domain`
- Domain은 Boundary를 참조하지 않는다.
- Domain은 UI/DB/Web/파일 시스템에 의존하지 않는다.

## 18. Component Candidates

| Component | Responsibility | Layer | Input | Output | Related FR | Related Test |
|---|---|---|---|---|---|---|
| BoundaryValidator | 입력 계약 검증 및 오류 코드 결정 | Boundary | `int[][]` | validation pass/fail | FR-01 | TC-EXC-001~004 |
| BlankFinder | row-major 기준 빈칸 2개 탐색 | Domain | validated matrix | blank positions(2) | FR-02 | TC-BND row-major 케이스 |
| MissingNumberFinder | 누락 숫자 2개 도출 및 오름차순 고정 | Domain | validated matrix | `(nSmall,nLarge)` | FR-03 | TC-DOM missing number |
| MagicSquareValidator | 행/열/대각선 합 34 판정 | Domain | completed candidate matrix | `boolean` | FR-04 | TC-NOR/TC-EXC-005 |
| Solver | two-combination 시도 및 성공/실패 결정 | Control/Domain | validated matrix + domain services | assignment or NO_VALID_ASSIGNMENT | FR-05 | TC-NOR-001/002, TC-EXC-005 |
| ResultFormatter | 성공 결과를 `int[6]`로 고정 형식 반환 | Boundary | assignment result | `[r1,c1,n1,r2,c2,n2]` | FR-05 | TC-BND-004/005 |

## 19. Risks & Ambiguities

| Risk | Impact | Decision / Mitigation |
|---|---|---|
| 1-index와 0-index 혼동 | 좌표 계약 위반 및 테스트 실패 | 출력 좌표는 1-index로 고정, Boundary 출력 테스트 필수 |
| row-major 첫 번째 빈칸 정의 누락 | small-first 기준점 불일치 | BR-05로 고정, Track B에서 독립 테스트 |
| small-first/ reverse 데이터 혼동 | 잘못된 기대치로 RED 품질 저하 | 대표 데이터셋을 TC-NOR-001/002로 분리 |
| 입력 행렬 변경 여부 불명확 | 부작용으로 회귀 발생 | NFR-04로 “입력 불변”을 명시 |
| 두 조합 모두 실패 정책 누락 | 호출자 계약 불안정 | `NO_VALID_ASSIGNMENT`로 단일 정책 고정 |
| 34 상수 하드코딩 난립 | 유지보수성 저하 | 명명 상수 정책 적용(`MAGIC_CONSTANT=34`) |
| Boundary와 Domain 책임 혼합 | 테스트 분리 불가 | ECB 의존 규칙 강제 및 Track 분리 테스트 |

## 20. Engineering Principles
- Python 코드는 PEP8과 type hints를 준수해야 한다.
- 테스트 프레임워크는 `pytest`를 사용하고 AAA 패턴을 따른다.
- TDD는 RED-GREEN-REFACTOR 순서를 강제한다.
- Domain Logic coverage 95%+, Boundary coverage 85%+를 유지한다.
- ECB 계층 분리 규칙을 준수한다.
  - 허용: `boundary -> control -> entity`
  - 금지: `boundary -> entity` 직접 의존, 역방향 의존, 순환 의존
- `print()` 기반 디버깅을 금지한다.
- `bare except` 또는 의도 없는 `except Exception`을 금지한다.
- 테스트 약화/삭제로 통과시키는 행위를 금지한다.
- 설명 없는 매직 넘버 사용을 금지한다.

## 21. Traceability Matrix

| Concept / Invariant | Business Rule | Feature ID | Acceptance Criteria | Test Case Candidate | Component |
|---|---|---|---|---|---|
| 4x4 입력 | BR-01 | FR-01 | AC-FR01-01 | TC-EXC-001 | BoundaryValidator |
| 빈칸 2개 | BR-02 | FR-01, FR-02 | AC-FR01-02, AC-FR02-01 | TC-EXC-002 | BoundaryValidator, BlankFinder |
| 값 범위 0 또는 1~16 | BR-03 | FR-01 | AC-FR01-03 | TC-EXC-003, TC-BND-001, TC-BND-002 | BoundaryValidator |
| 중복 금지 | BR-04 | FR-01 | AC-FR01-04 | TC-EXC-004 | BoundaryValidator |
| row-major 첫 번째 빈칸 | BR-05 | FR-02 | AC-FR02-02 | TC-DOM-Blank-RowMajor | BlankFinder |
| 누락 숫자 2개 | BR-06 | FR-03 | AC-FR03-01 | TC-DOM-Missing-Count | MissingNumberFinder |
| 누락 숫자 오름차순 | BR-07 | FR-03 | AC-FR03-02 | TC-DOM-Missing-Ascending | MissingNumberFinder |
| 마방진 상수 34 | BR-08 | FR-04 | AC-FR04-01 | TC-DOM-Validate-34 | MagicSquareValidator |
| 행/열/대각선 합 | BR-09 | FR-04 | AC-FR04-01, AC-FR04-02 | TC-DOM-Validate-RowColDiag | MagicSquareValidator |
| Boundary pre-check / Domain 미호출 | BR-01~BR-04 | FR-01 | AC-FR01-05 | TC-UI-Domain-Not-Called | BoundaryValidator |
| small-first 시도 | BR-10 | FR-05 | AC-FR05-01 | TC-NOR-001 | Solver |
| reverse 시도 | BR-11 | FR-05 | AC-FR05-02 | TC-NOR-002 | Solver |
| No valid assignment | BR-10, BR-11 | FR-05 | AC-FR05-03 | TC-EXC-005 | Solver |
| int[6] 반환 | BR-13 | FR-05 | AC-FR05-04 | TC-BND-005 | ResultFormatter |
| 1-index 좌표 | BR-12 | FR-05 | AC-FR05-04 | TC-BND-004 | ResultFormatter |

## 22. Open Questions / Decision Needed
- 없음. 본 PRD에서는 다음을 확정했다.
  - 대각선 포함 마방진 판정 사용
  - 두 조합 실패 정책은 `NO_VALID_ASSIGNMENT` 오류 응답
  - 입력 행렬은 변경하지 않음(No side effects)

## 23. Appendix

### 23.1 참고 문서 목록
- `Report/01. 4x4_MagicSquare_Problem_Definition_Report.md`
- `Report/02. 4x4_MagicSquare_Dual-Track_TDD_CleanArchitecture_Design_Report.md`
- `Report/03. MagicSquare_CursorRules_and_UserEntity_Implementation_Report.md`
- `Report/04. MagicSquare_Level1-5_UserJourney_Story_Scenario_Verification_Report.md`
- `.cursorrules`
- `.cursor/rules/magicsquare-project.mdc`
- `.cursor/rules/magicsquare-ecb-architecture.mdc`
- `.cursor/rules/magicsquare-python-code-style.mdc`
- `.cursor/rules/magicsquare-tdd-testing.mdc`
- `.cursor/rules/magicsquare-forbidden.mdc`

### 23.2 Cursor Rules 요약
- 프로젝트 목적: ECB + Dual-Track TDD 기반 유지보수 가능한 코드
- 테스트 우선: 관련 테스트 확인 후 최소 구현
- 아키텍처: Boundary/Control/Entity 의존 방향 강제
- 코드 품질: PEP8, type hints, 명확한 명명
- 금지: `print()`, 설명 없는 매직넘버, 예외 무시, 테스트 약화

### 23.3 대표 Gherkin Scenario 요약
- Scenario-GRK-001 (small-first 성공)  
  Given 유효한 4x4 입력과 빈칸 2개  
  When small-first를 적용한다  
  Then 결과는 `int[6]` 형식으로 반환된다.
- Scenario-GRK-002 (reverse 성공)  
  Given small-first로는 마방진이 되지 않는 유효 입력  
  When reverse 조합을 적용한다  
  Then reverse 순서 결과를 반환한다.
- Scenario-GRK-003 (입력 오류 차단)  
  Given 계약 위반 입력  
  When Boundary가 검증한다  
  Then Domain resolver는 호출되지 않고 표준 오류를 반환한다.
- Scenario-GRK-004 (두 조합 모두 실패)  
  Given 유효 입력이나 두 조합 모두 실패  
  When Solver가 시도한다  
  Then `NO_VALID_ASSIGNMENT`를 반환한다.

### 23.4 향후 RED Test ID 후보
- Track A: `TA-RED-001`~`TA-RED-010` (입력 검증/출력 형식/도메인 미호출)
- Track B: `TB-RED-001`~`TB-RED-015` (빈칸 탐색/누락 숫자/판정/두 조합)
- 통합 회귀: `TI-RED-001`~`TI-RED-006` (계약 보존/실패 코드 보존)
