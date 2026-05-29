# MagicSquare_xxx

4×4 **마방진(Magic Square)** 을 도메인으로, **TDD 구현 역량**을 훈련하는 학습 프로젝트입니다.  
핵심은 정답 알고리즘을 빨리 만드는 것이 아니라, **계약 고정 -> 테스트 우선 -> 리팩토링**을 반복하며 안정적으로 개발하는 것입니다.

| 항목 | 내용 |
|------|------|
| **현재 단계** | AC-FR-01-01 **GREEN 완료** · M1-GUI **셸 구현** → Dual-Track GREEN 진행 중 |
| **1차 범위** | 4×4 입력 계약 기반 **해결 결과 산출** |
| **훈련 초점** | Domain 중심 설계 + Contract-first 테스트 |
| **TDD 진행** | RED 설계 묶음 **17**개 중 GREEN **4**개 (커밋) · 테스트 **9/33** 통과 |
| **상태** | AC-FR-01-01 **4커밋 GREEN** 완료 — GUI(`boundary/screen/`) **셸 구현** (`python -m boundary.screen.app`) |

---

## 프로젝트 정의

이 프로젝트는 “마방진 문제” 자체를 끝내는 프로젝트가 아니라, 다음을 반복 훈련하는 **TDD 실습 프로젝트**입니다.

- Domain 규칙을 계약으로 명시하는 능력
- 레이어 경계를 분리해 변경 영향을 제어하는 능력
- RED-GREEN-REFACTOR 사이클로 구현 품질을 유지하는 능력
- 회귀 테스트로 리팩토링 안전성을 확보하는 능력

### 한 줄 정의

> **마방진은 학습 도메인이고, 진짜 산출물은 TDD로 검증 가능한 구현 프로세스다.**

---

## 프로젝트 목적

### Product 목적 (무엇을 만든다)

- 고정 입력 계약을 받아 고정 출력 계약으로 결과를 산출하는 모듈을 만든다.
- 결과의 일관성과 재현성을 테스트로 증명한다.

### Process 목적 (어떻게 만든다)

- 구현 전에 테스트와 계약을 먼저 고정한다.
- Domain -> UI Boundary -> Data -> Integration 순서로 확장한다.
- 각 단계에서 RED-GREEN-REFACTOR 완료 기준을 통과한다.

---

## 학습 목표 (측정 가능한 기준)

| 목표 ID | 목표 | 측정 기준 |
|---|---|---|
| `G-01` | 계약 기반 설계 숙련 | 입력/출력/오류 계약 테스트 100% 통과 |
| `G-02` | 레이어 분리 숙련 | Domain이 UI/Data 구현체에 의존하지 않음 |
| `G-03` | TDD 사이클 숙련 | 기능 단위마다 RED->GREEN->REFACTOR 기록 유지 |
| `G-04` | 회귀 안정성 확보 | 리팩토링 후 전체 테스트 상시 그린 |
| `G-05` | 변경 통제 능력 확보 | 계약/출력 포맷 변경 시 영향 테스트 동반 |

---

## 성공 기준 (Done at Project Level)

- [ ] 고정 계약을 깨는 변경이 없다.
- [ ] Domain/UI/Data/Integration 테스트 스위트가 모두 통과한다.
- [ ] 신규 기능 추가 시 기존 테스트 삭제 없이 확장된다.
- [ ] 리팩토링 커밋 이후에도 결과 포맷과 오류 코드가 유지된다.
- [ ] README, Report, 테스트 명세 간 불일치가 없다.

---

## 고정 계약 (변경 금지)

### 입력 계약

- 타입: `int[4][4]`
- `0`은 빈칸이며, 빈칸 개수는 정확히 2개
- 값 범위: `0` 또는 `1~16`
- `0` 제외 중복 금지

### 출력 계약

- 타입: `int[6]`
- 형식: `[r1,c1,n1,r2,c2,n2]`
- 좌표는 1-index
- `n1,n2`는 누락 숫자 2개이며,
  - `(작은수 -> 첫 빈칸, 큰수 -> 둘째 빈칸)` 조합이 마방진이면 해당 순서
  - 아니면 반대 순서

---

## 프로젝트 배경

- 도메인은 **4×4 마방진**이며, 입력은 4×4 정수 행렬(0은 빈칸)입니다.
- 구현 목표는 단일 알고리즘 과시가 아니라, **명확한 계약(입력/출력/오류)과 테스트 우선 개발**입니다.
- 학습 목표는 **Clean Architecture 경계 유지**와 **RED-GREEN-REFACTOR 사이클 숙련**입니다.

### 도메인 vs 학습 목표

| 구분 | 내용 |
|------|------|
| **도메인(What)** | 4×4 마방진 규칙(행/열/대각선 합, 값 집합) |
| **학습 목표(How)** | TDD로 계약을 고정하고 테스트로 구현을 진화 |
| **아키텍처 목표(Structure)** | Logic/UI Boundary/Data 인터페이스 분리 |

---

## 방법론 (STEP 1 ~ 5)

문제를 바로 구현하지 않고, 아래 순서로 **관찰 → 동기(Why) → TDD적 사고 → 진짜 문제 정의**까지 진행했습니다.

| STEP | 제목 | 요약 |
|------|------|------|
| **1** | Observation (관찰) | 상황·맥락·미확정 항목 고정 |
| **2** | Why #1 | 왜 “완성”이 필요한가 — 불편함·구조적 문제 |
| **3** | Why #2 | 왜 손계산이 아니라 프로그램인가 — 반복·자동화·오류 방지 |
| **4** | Why #3 | 왜 TDD 방식인가 — 통제·불변·입출력 명확성 |
| **5** | 진짜 문제 정의 | 표면/개선 정의, Invariant, 훈련 목표 |

```mermaid
flowchart LR
  S1[STEP1 관찰] --> S2[STEP2 Why1]
  S2 --> S3[STEP3 Why2]
  S3 --> S4[STEP4 TDD]
  S4 --> S5[STEP5 정의]
  S5 --> N[다음: 합의·시나리오·구현]
```

---

## 1차 범위 (In / Out)

### In scope

- 입력 계약 검증: 4×4, 0은 정확히 2개, 값 범위 0/1~16, 0 제외 중복 금지
- 도메인 규칙 검증: 행/열/대각선 합과 Magic Constant 기반 판정
- 출력 계약 고정: `int[6] = [r1,c1,n1,r2,c2,n2]` (1-index)
- 레이어 분리: Logic / UI Boundary / Data(저장/로드 인터페이스)
- 테스트 우선 구현: Domain, UI Contract, Data, Integration 시나리오

### Out of scope (1차)

- 고급 최적화/휴리스틱 탐색
- 원격 DB/네트워크 영속성
- 3×3, 5×5 등 다른 차수 일반화

### 별도 스프린트 (TDD Track)

- **그래픽 UI** (`boundary/screen/`) — PyQt6 셸 **구현 완료** (크기 검증 표시·샘플 격자·풀이 시도). `test_gui_*.py` RED·풀이 GREEN 연동은 후속. 아래 [GUI 실행](#gui-실행) 참고.

### 합의 전 (TBD)

- [ ] Domain 에러를 UI 표준 에러로 매핑하는 레벨(코드만/메시지 포함)
- [ ] Data Layer 기본 저장 범위(입력만/결과 포함)
- [ ] Application Service 레이어를 1차에 포함할지 여부
- [ ] File 어댑터 포맷(JSON 단일/CSV 허용)

---

## 핵심 Invariant (요약)

판정 규칙이 깨지면 안 되는 조건입니다. 상세는 보고서 STEP 5를 참고하세요.

| ID | 불변 |
|----|------|
| **D1** | 격자는 4×4 |
| **D2** | 입력 단계: 값은 0 또는 1~16, 0은 정확히 2개, 0 제외 중복 금지 |
| **D3** | 완성 후보 단계: 값 집합은 1~16 각 1회 |
| **D4~D6** | 완성 후보 단계에서 각 행·열·두 대각선 합 = 34 |
| **D7** | D3~D6 **모두** 만족 시에만 “마방진 완성” |
| **S1~S5** | 재현성, 격자만으로 판정, 회귀, 주장–규칙 일치, 생성 경로 무관 |
| **T1~T3** | 참·거짓 오라클, 규칙 변경 시 기대 문서화 |

---

## 저장소 구조

```
MagicSquare_xxx/
├── README.md                 ← 이 파일 (프로젝트 진입점)
├── requirements-gui.txt      ← PyQt6 GUI 의존성 (pytest와 분리)
├── Report/
│   └── 01. 4x4_MagicSquare_Problem_Definition_Report.md
│   └── 02. 4x4_MagicSquare_Dual-Track_TDD_CleanArchitecture_Design_Report.md
│   └── 03. MagicSquare_CursorRules_and_UserEntity_Implementation_Report.md
│   └── 04. MagicSquare_Level1-5_UserJourney_Story_Scenario_Verification_Report.md
│   └── 05. MagicSquare_AC_FR_01_01_RED_Test_Implementation_Report.md
│   └── 06. MagicSquare_FR01_FR05_DualTrack_RED_Design_Report.md
│   └── 09. MagicSquare_DualTrack_RED_Skeleton_Test_Implementation_Report.md
│   └── 10. MagicSquare_AC_FR_01_01_GREEN_Test_Implementation_Report.md
│   └── 11. MagicSquare_AC_FR_01_01_Split_GREEN_TDD_Progress_Report.md
│   └── 12. MagicSquare_M1_GUI_PyQt_Implementation_Report.md
├── boundary/                  ← Boundary 최소 구현 (AC-FR-01-01 GREEN)
│   ├── validator.py           # BoundaryValidator.validate()
│   ├── schemas.py             # pydantic ErrorResponse
│   ├── constants.py           # GRID_SIZE
│   └── screen/                # PyQt6 GUI (M1-GUI 셸)
│       ├── app.py             # python -m boundary.screen.app
│       ├── main_window.py     # 4×4 입력·결과 패널
│       ├── presenter.py       # ScreenPresenter (boundary/control 어댑터)
│       └── sample_grids.py    # G0~G2 샘플 격자
├── control/                   ← Control 최소 구현 (AC-FR-01-01 GREEN)
│   ├── resolver.py            # MagicSquareResolver
│   └── factory.py             # create_magic_square_resolver()
├── entity/                    ← Domain 스텁 + UserEntity
├── tests/                     ← pytest 70건 (Report/09 GREEN + GM 17 + 보조 11)
├── test_plan.md
├── defect_list.md
└── Prompt/
    └── 01. 4x4_MagicSquare_Problem_Definition_Report_Prompt.md
    └── 02. MagicSquare_4x4_TDD_Interactive_Prompt_Transcript.md
    └── 03. MagicSquare_CursorRules_UserEntity_Interactive_Prompt_Transcript.md
    └── 04. MagicSquare_Level1-5_Interactive_Prompt_Transcript.md
    └── 05. MagicSquare_AC_FR_01_01_Interactive_Prompt_Transcript.md
    └── 06. MagicSquare_FR01_FR05_DualTrack_RED_Design_Interactive_Prompt_Transcript.md
    └── 12. MagicSquare_M1_GUI_PyQt_Interactive_Prompt_Transcript.md
```

| 경로 | 설명 |
|------|------|
| [Report/01. 4x4_MagicSquare_Problem_Definition_Report.md](Report/01.%204x4_MagicSquare_Problem_Definition_Report.md) | STEP 1~5 **통합 보고서** (목차·상세 분석·합의 체크리스트) |
| [Report/02. 4x4_MagicSquare_Dual-Track_TDD_CleanArchitecture_Design_Report.md](Report/02.%204x4_MagicSquare_Dual-Track_TDD_CleanArchitecture_Design_Report.md) | Dual-Track UI+Logic TDD + Clean Architecture **설계 보고서** |
| [Report/03. MagicSquare_CursorRules_and_UserEntity_Implementation_Report.md](Report/03.%20MagicSquare_CursorRules_and_UserEntity_Implementation_Report.md) | Cursor Rules 반영 + UserEntity 구현 관련 **결과 보고서** |
| [Report/04. MagicSquare_Level1-5_UserJourney_Story_Scenario_Verification_Report.md](Report/04.%20MagicSquare_Level1-5_UserJourney_Story_Scenario_Verification_Report.md) | Level 1~5(Epic/Journey/Story/Scenario/Verification) **통합 검증 보고서** |
| [Report/05. MagicSquare_AC_FR_01_01_RED_Test_Implementation_Report.md](Report/05.%20MagicSquare_AC_FR_01_01_RED_Test_Implementation_Report.md) | AC-FR-01-01 RED 테스트·실패 분석 **구현 보고서** |
| [Report/06. MagicSquare_FR01_FR05_DualTrack_RED_Design_Report.md](Report/06.%20MagicSquare_FR01_FR05_DualTrack_RED_Design_Report.md) | FR-01~FR-05 Dual-Track **RED 설계표** 보고서 |
| [Report/09. MagicSquare_DualTrack_RED_Skeleton_Test_Implementation_Report.md](Report/09.%20MagicSquare_DualTrack_RED_Skeleton_Test_Implementation_Report.md) | Dual-Track RED **스켈레톤 pytest** 구현 보고서 (24건) |
| [Report/10. MagicSquare_AC_FR_01_01_GREEN_Test_Implementation_Report.md](Report/10.%20MagicSquare_AC_FR_01_01_GREEN_Test_Implementation_Report.md) | AC-FR-01-01 **GREEN** 구현 보고서 (9건 통과) |
| [Report/11. MagicSquare_AC_FR_01_01_Split_GREEN_TDD_Progress_Report.md](Report/11.%20MagicSquare_AC_FR_01_01_Split_GREEN_TDD_Progress_Report.md) | 분할 GREEN 4커밋·TDD 진행 현황·GUI 검토 **통합 보고서** |
| [Report/12. MagicSquare_M1_GUI_PyQt_Implementation_Report.md](Report/12.%20MagicSquare_M1_GUI_PyQt_Implementation_Report.md) | M1-GUI PyQt6 셸 **구현 보고서** |
| [Report/14. MagicSquare_Refactoring_Plan_Report.md](Report/14.%20MagicSquare_Refactoring_Plan_Report.md) | REFACTOR 사전 분석·계획 |
| [Report/15. MagicSquare_REFACTOR_P0_Implementation_Report.md](Report/15.%20MagicSquare_REFACTOR_P0_Implementation_Report.md) | REFACTOR P0 **구현**·회귀 검증 |
| [Report/16. MagicSquare_Coverage_Gate_GREEN_QA_Report.md](Report/16.%20MagicSquare_Coverage_Gate_GREEN_QA_Report.md) | 커버리지 Gate GREEN · QA 분석 **구현 보고서** |
| [test_plan.md](test_plan.md) | FR-01 입력 크기 검증 **테스트 계획서** |
| [defect_list.md](defect_list.md) | RED 단계 **결함 목록** (DEF-001~010) |
| [Prompt/01. 4x4_MagicSquare_Problem_Definition_Report_Prompt.md](Prompt/01.%204x4_MagicSquare_Problem_Definition_Report_Prompt.md) | 동일 워크플로 **재실행용** 대화형 프롬프트 transcript |
| [Prompt/02. MagicSquare_4x4_TDD_Interactive_Prompt_Transcript.md](Prompt/02.%20MagicSquare_4x4_TDD_Interactive_Prompt_Transcript.md) | 현재 요구 반영 **대화형 실행 프롬프트 export** |
| [Prompt/03. MagicSquare_CursorRules_UserEntity_Interactive_Prompt_Transcript.md](Prompt/03.%20MagicSquare_CursorRules_UserEntity_Interactive_Prompt_Transcript.md) | Cursor Rules/UserEntity 관련 **대화형 프롬프트 export** |
| [Prompt/04. MagicSquare_Level1-5_Interactive_Prompt_Transcript.md](Prompt/04.%20MagicSquare_Level1-5_Interactive_Prompt_Transcript.md) | Level 1~5 설계/검증 흐름 **대화형 프롬프트 export** |
| [Prompt/05. MagicSquare_AC_FR_01_01_Interactive_Prompt_Transcript.md](Prompt/05.%20MagicSquare_AC_FR_01_01_Interactive_Prompt_Transcript.md) | AC-FR-01-01 RED 테스트 **대화형 프롬프트 export** |
| [Prompt/06. MagicSquare_FR01_FR05_DualTrack_RED_Design_Interactive_Prompt_Transcript.md](Prompt/06.%20MagicSquare_FR01_FR05_DualTrack_RED_Design_Interactive_Prompt_Transcript.md) | FR-01~FR-05 RED 설계 **대화형 프롬프트 export** |
| [Prompt/07. MagicSquare_DualTrack_RED_Skeleton_Interactive_Prompt_Transcript.md](Prompt/07.%20MagicSquare_DualTrack_RED_Skeleton_Interactive_Prompt_Transcript.md) | Dual-Track RED 스켈레톤 **대화형 프롬프트 export** |
| [Prompt/10. MagicSquare_AC_FR_01_01_GREEN_Interactive_Prompt_Transcript.md](Prompt/10.%20MagicSquare_AC_FR_01_01_GREEN_Interactive_Prompt_Transcript.md) | AC-FR-01-01 일괄 GREEN **대화형 프롬프트 export** |
| [Prompt/11. MagicSquare_AC_FR_01_01_Split_GREEN_TDD_Progress_Interactive_Prompt_Transcript.md](Prompt/11.%20MagicSquare_AC_FR_01_01_Split_GREEN_TDD_Progress_Interactive_Prompt_Transcript.md) | 분할 GREEN·TDD 진행·GUI 검토 **대화형 프롬프트 export** |
| [Prompt/12. MagicSquare_M1_GUI_PyQt_Interactive_Prompt_Transcript.md](Prompt/12.%20MagicSquare_M1_GUI_PyQt_Interactive_Prompt_Transcript.md) | M1-GUI PyQt6 구현·실행 **대화형 프롬프트 export** |
| [Prompt/14. MagicSquare_Refactoring_Plan_Interactive_Prompt_Transcript.md](Prompt/14.%20MagicSquare_Refactoring_Plan_Interactive_Prompt_Transcript.md) | REFACTOR 계획 **대화형 프롬프트 export** |
| [Prompt/15. MagicSquare_REFACTOR_P0_Interactive_Prompt_Transcript.md](Prompt/15.%20MagicSquare_REFACTOR_P0_Interactive_Prompt_Transcript.md) | REFACTOR P0 구현 **대화형 프롬프트 export** |
| [Prompt/16. MagicSquare_Coverage_Gate_GREEN_Interactive_Prompt_Transcript.md](Prompt/16.%20MagicSquare_Coverage_Gate_GREEN_Interactive_Prompt_Transcript.md) | 커버리지 Gate GREEN · QA **대화형 프롬프트 export** |

---

## 문서 읽는 순서

1. **README.md** (현재) — 개요·범위·다음 단계  
2. **Report** — STEP별 상세 논의·불변·사고 훈련 목표  
3. **Prompt** — 새 AI 세션에서 설계 문서 작성을 재실행할 때 USER 프롬프트 복사  

---

## 진행 방법 (RED-GREEN-REFACTOR)

이 프로젝트의 구현 단계는 아래 규칙을 필수로 따릅니다.

### RED

- 먼저 실패 테스트를 작성한다. (구현 코드 선작성 금지)
- 테스트는 계약/불변조건/출력 형식을 검증해야 한다.
- 테스트 ID를 부여한다. (`T-DOM-*`, `T-UI-*`, `T-DAT-*`, `T-INT-*`)
- RED 종료 조건: “의도한 이유로 실패하는 테스트”가 확보되어야 한다.

### GREEN

- RED 테스트를 통과하는 최소 구현만 추가한다.
- 과도한 추상화/최적화는 금지한다.
- GREEN 종료 조건: 해당 사이클 대상 테스트가 모두 통과해야 한다.

### REFACTOR

- 동작 변경 없이 구조만 개선한다.
- 레이어 경계(Logic/UI/Data)와 계약 형식은 변경하지 않는다.
- 리팩토링 전후 전체 테스트를 실행해 회귀를 확인한다.
- REFACTOR 종료 조건: 테스트 전부 통과 + 중복/복잡도 감소가 확인되어야 한다.

### 사이클 운영 규칙

- 한 사이클에는 하나의 학습 목표만 포함한다. (예: 입력 검증, 순서 정책)
- **RED 커밋**: 설계 묶음 1개당 실패 테스트 1커밋.
- **GREEN 커밋**: 대응 RED 묶음 1개당 최소 구현 1커밋. **REFACTOR는 같은 커밋에 포함하지 않는다.**
- 커밋 단위는 `RED -> GREEN -> REFACTOR` 흐름을 추적 가능하게 유지한다.
- 계약 변경이 필요한 경우, 먼저 테스트/문서를 갱신한 뒤 구현을 수정한다.

### 설계 묶음 vs 커밋 묶음

| 구분 | 의미 | AC-FR-01-01 예 |
|------|------|----------------|
| **설계 묶음** | `test_plan` / Report/05의 TA-RED 단위 (기능·테스트 추적) | R-05-01 ~ R-05-05 (5묶음) |
| **커밋 묶음** | git에 실제로 남긴 RED/GREEN 커밋 단위 | GREEN **4커밋** (아래 표) |

> Report/05 최초 RED는 9건 **1커밋**(`352cd24`), 최초 GREEN도 **1커밋**(`aa10473`)이었음.  
> 이후 `stabilize/green` 브랜치에서 **RED 묶음별 GREEN 4커밋**으로 재적용함 (`bc022cb` ~ `d0fe1e2`).

---

## RED 단계 To-Do 리스트

> Track A/B 체크리스트·커버리지 목표·`defect_list.md` 연결은 [TDD 진행 현황](#tdd-진행-현황-red-묶음--green-목표) 및 `test_plan.md`를 참고한다.

## Golden Master 회귀 안전장치

Refactoring 시작 전 구축.  
GREEN 완료 후 즉시 적용.

### 기준 파일 생성

- GM-01: `golden_master_expected.txt` 생성
- GM-02: 정상/역순/오류 시나리오 추가
- GM-03: `git add tests/golden_master_expected.txt`

### 테스트 코드

- GM-04: `test_golden_master_magic_square` 작성
- GM-05: approve 패턴 적용
- GM-06: Golden Master 테스트 PASS 확인

```powershell
python -m pytest tests/test_golden_master_magic_square.py -m golden_master -v
# → 17 passed (GM-TC-01~05 + 계약 검증)
```

### 회귀 보호

- GM-07: row-major 규칙 보호
- GM-08: 1-index 출력 보호
- GM-09: reverse 조합 fallback 보호
- GM-10: Error Contract 보호

> 상세 approve 패턴·시나리오 정의: `docs/golden_master_approve_pattern.md`

---

## REFACTOR To-Do 리스트

> **SSOT:** [Report/14](Report/14.%20MagicSquare_Refactoring_Plan_Report.md) (계획) · [Report/15](Report/15.%20MagicSquare_REFACTOR_P0_Implementation_Report.md) (P0 구현)  
> **회귀 안전망 (매 커밋):** GREEN 33 + Golden Master 17  
> **실행 순서:** C(P0) → A(P0) → B(P0) → A(P1)+B(P1) → C(P1) → B(P2)

### 그룹 C — 테스트·기반 시설

**목표:** pytest 수집 복구 → 리팩토링 후 회귀 검증 가능 상태

#### P0 — 수집 오류 복구

- [x] `tests/entity/test_d_mis_01_missing_numbers.py` — `missing_number_finder` → `missing_numbers` import 정렬
- [x] `tests/entity/test_d_sol_01_04_solution.py` — `control.solver` → `entity.solver` import 정렬
- [x] `tests/boundary/test_u_flow_02_execute_zero_calls.py` — `ui_boundary`·`solve_partial` 구현 후 import 연결
- [x] `tests/boundary/test_u_out_01_03_output_contract.py` — `ui_boundary` 구현 후 import 연결
- [x] `pytest tests/` — collection error **0건** 확인

#### P1 — RED 스켈레톤 GREEN 전환

> 진행 SSOT: [커버리지 Gate To-Do](#커버리지-gate-to-do)

- [x] `test_u_in_04_08_input_validation.py` — U-IN-04~08 (5건) → Gate ③
- [x] `test_d_loc_01_blank_coords.py` — D-LOC-01 (1건) + D-LOC-02
- [x] `test_d_val_01_06_magic_square.py` — D-VAL-01~06 (6건)
- [x] `test_d_mis_01_missing_numbers.py` — D-MIS-01 (1건) + D-MIS-02 *(P1 Track B)*
- [x] `test_d_sol_01_04_solution.py` — D-SOL-01~04 (4건) → Gate ②
- [x] `test_u_flow_02_execute_zero_calls.py` — U-FLOW-02 (4건) → Gate ④
- [x] `test_u_out_01_03_output_contract.py` — U-OUT-01~03 (3건) → Gate ⑤
- [x] `test_screen_presenter.py` — ScreenPresenter 계약 (7건, PyQt 불필요)
- [x] `test_gui_invalid_size_message.py` — GUI INVALID_SIZE SSOT (Report/12)
- [x] `test_error_messages.py` — envelope fallback
- [x] `test_resolver_happy_path.py` · `test_factory.py` — Control happy path

#### 회귀 기준 (리팩토링 대상 아님 — 매 커밋 검증)

- [x] AC-FR-01-01 9건 (boundary 7 + control 2)
- [x] Golden Master 17건

---

### 그룹 A — 아키텍처·의존성 정렬 (ECB)

**목표:** 레이어 경계 복원, GUI·Pipeline 단일 풀이 경로 확립

**목표 흐름:** `Screen → UIBoundary → SolvePartialMagicSquare → entity/services/*`

#### P0

- [x] `boundary/ui_boundary.py` — `UIBoundary` Facade (validate/solve; envelope E001~E007 후속)
- [x] `control/solve_partial.py` — `execute` + `NoValidAssignmentError` 매핑
- [x] `boundary/screen/presenter.py`, `main_window.py` — UIBoundary 위임, Control 직접 import 제거
- [x] `boundary/pipeline.py` — `control/pipeline` → boundary 이동, Golden Master import 갱신
- [x] `boundary/input_validator.py` — `boundary→entity` 제거 (`boundary.constants` 사용)

#### P1

- [ ] `entity/solver.py` — Entity/Control 혼재 해소 → `two_cell_solver` 추출
- [ ] `control/resolver.py` — E001 Control·Boundary 이중 책임 정리 (Collapse Hierarchy)

---

### 그룹 B — 책임·계약·코드 품질 (SRP / DTO / VO)

**목표:** 단일 책임 정리, 오류·출력 계약 통합 (E001~E007·int[6] 불변)

#### P0

- [x] `boundary/validator.py` — `NotImplementedError` → `ErrorResponse | None` 반환
- [x] `boundary/pipeline.py` — size 검증 예외 흐름 제거
- [x] `boundary/screen/presenter.py` — `NotImplementedError` catch 제거

#### P1

- [ ] `boundary/input_validator.py` — 검증 + ErrorResponse envelope 역할 분리
- [ ] `control/resolver.py`, `boundary/validator.py` — `ErrorResponse`/`ResolveError`, `INVALID_SIZE` DTO 통합
- [ ] `entity/solver.py`, `presenter.py` — `int[6]` primitive → `Solution` Value Object
- [ ] `boundary/screen/main_window.py` — View + fixture 주입 분리

#### P2

- [ ] `entity/constants.py`, `boundary/constants.py`, `boundary/screen/` — `GRID_SIZE` 등 상수 SSOT 통합
- [ ] `entity/services/magic_square_validator.py` — 단일 함수 다중 불변식 Extract Method
- [ ] `entity/solver.py` — 4×4 `deepcopy` 단순화
- [ ] `entity/user.py` — 도메인 무관 코드 정리 (Move Class / Remove Dead Code)

---

### REFACTOR Go/No-Go

- [x] `pytest tests/` — collection error 0건
- [x] **70 passed** + Golden Master 17 PASS ([Report/16](Report/16.%20MagicSquare_Coverage_Gate_GREEN_QA_Report.md))
- [x] AC-FR-01-01 9건 PASS
- [x] ECB 역의존 import 0건 (`boundary→entity`, `control→boundary`, Screen→Control)
- [x] RED 스켈레톤 16건 → **0건** (70 passed, 2026-05-29)
- [ ] E001~E007 code/message, int[6] 계약 불변
- [ ] GUI 수동 체크 — `python -m boundary.screen.app` INVALID_SIZE 메시지 SSOT 일치

---

## 로컬 실행 (현재 구현 범위)

### 환경 준비

```powershell
cd c:\dev\MagicSquare_xxx
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install pytest pydantic pytest-cov
```

GUI 실행 시 추가:

```powershell
pip install -r requirements-gui.txt
```

### pytest — 회귀 기준선 (AC-FR-01-01)

```powershell
python -m pytest tests/boundary/test_ac_fr_01_01_matrix_size.py tests/control/test_ac_fr_01_01_domain_isolation.py -v
# → 9 passed
```

### GUI — PyQt6 앱 실행

```powershell
python -m boundary.screen.app
```

창 제목 **MagicSquare — 4×4 마방진**이 표시됩니다.

### Python — Boundary 계약 직접 호출 (GUI 없이 확인)

현재 구현으로 **터미널에서 즉시 실행** 가능한 범위는 크기 검증뿐입니다.

```powershell
python -c "from boundary import BoundaryValidator; r=BoundaryValidator().validate(None); print(r.code, r.message)"
# INVALID_SIZE Grid must be 4x4.
```

유효 4×4 격자는 `NotImplementedError` (AC-FR-01-01 범위 외). 퍼즐 풀이·성공 경로는 Report/09 Logic GREEN 이후입니다.

---

## GUI 실행

### 현재 상태

| 항목 | 상태 |
|------|------|
| `boundary/screen/` | ✅ PyQt6 GUI 셸 구현 |
| `requirements-gui.txt` | ✅ PyQt6>=6.6.0 (pytest와 분리) |
| `python -m boundary.screen.app` | ✅ 실행 가능 |
| `boundary/ui_boundary.py` (`UIBoundary`) | ❌ 미구현 — Report/09 스켈레톤 import 대기 |
| pytest Boundary 계약 | **9건 PASS** — GUI 크기 검증 메시지 SSOT 일치 |
| `test_gui_*.py` | ❌ 미작성 — GUI 자동화 테스트 후속 |

### ECB 구조 (구현됨)

```text
boundary/screen/main_window.py   ← PyQt View (위젯·이벤트·표시)
    ↓
boundary/screen/presenter.py     ← ScreenPresenter
    ↓                    ↓
boundary/validator.py   control/resolver.py
                              ↓
                        entity/solver.py (control/factory.py 경유)
```

- **screen → entity 직접 import 금지** — `presenter`는 `control.factory`만 사용
- **control/entity에 PyQt import 금지** — UI는 `boundary/screen/`에만
- GUI는 **비즈니스 로직을 복제하지 않고** `BoundaryValidator.validate()` SSOT 호출

### GUI 기능

| 영역 | 내용 |
|------|------|
| **입력** | 4×4 `QSpinBox` (0~16, 0=빈칸) |
| **샘플** | G0(완성), G1(small-first), G2(reverse), 빈 격자 — Report/06 §5 |
| **크기 검증** | `BoundaryValidator` — pytest와 동일 `INVALID_SIZE` 메시지 |
| **검증 시나리오** | 현재 격자 / null / `[]` / 3×4 |
| **풀이** | `MagicSquareResolver` — solver 스텁 시 미구현 안내 |
| **결과** | 상태 라벨 · 상세 텍스트 · 풀이 후 격자 미리보기 |

### 수동 확인 체크리스트

- [ ] `python -m boundary.screen.app` — 창 표시
- [ ] 검증 시나리오 `null` → `Grid must be 4x4.` (pytest `INVALID_SIZE_MESSAGE`와 동일)
- [ ] 샘플 G1 로드 → 크기 검증 통과
- [ ] G1 풀이 → `MagicSquareSolver.resolve is not implemented.` 안내
- [ ] AC-FR-01-01 pytest 9건 PASS

### GUI에서 보여줄 수 있는 것 / 없는 것

| 입력·동작 | GUI 표시 | 백엔드 |
|-----------|----------|--------|
| null / `[]` / 3×4 (검증 시나리오) | `[INVALID_SIZE] Grid must be 4x4.` | ✅ `BoundaryValidator` |
| 유효 4×4 + 크기 검증 | `Grid size is valid (4×4).` | ✅ |
| G1 + 풀이 | 미구현 안내 | ❌ `MagicSquareSolver` 스텁 |
| 빈칸 3개 등 | E002 등 | ❌ Report/09 U-IN 미GREEN |
| G1 성공 `int[6]` | 풀이 후 격자 채움 | ❌ D-SOL GREEN 후 자동 연동 예정 |

### GUI TDD 후속 (권장)

| 순서 | 작업 | 커밋 예 |
|:---:|------|---------|
| 1 | `tests/boundary/test_gui_*.py` RED — INVALID_SIZE 메시지 문자열 SSOT | `test(red): GUI shows INVALID_SIZE message` |
| 2 | GUI 메시지 회귀 GREEN | `test(green): GUI validator message contract` |
| 3 | D-SOL GREEN마다 풀이 결과·격자 표시 연동 | 묶음별 커밋 |

GUI는 **AC-FR-01-01 GREEN 4커밋과 분리**하는 것이 원칙입니다 (기능 GREEN 커밋에 PyQt 섞지 않음).

---

## TDD 진행 현황 (RED 묶음 · GREEN 목표)

> **요약: 모든 RED 묶음의 GREEN을 끝낸 상태가 아닙니다.**  
> Report/05(AC-FR-01-01) 설계 묶음 **5개** · 테스트 **9건** GREEN 완료 (**git GREEN 커밋 4개**).  
> Report/09 스켈레톤 **12개 묶음 · 24개 테스트**는 RED만 존재.

### AC-FR-01-01 GREEN 커밋 이력 (`stabilize/green`)

| 커밋 | 묶음 | test_plan | 통과 테스트 |
|------|------|-----------|-------------|
| `bc022cb` | green-1 | TA-RED-001 | `test_none_grid_returns_invalid_size_code_message` |
| `f1e6632` | green-2 | TA-RED-002~004 | `test_empty_list_grid_...`, `test_four_empty_rows_...`, `test_3x4_grid_...` |
| `6ac6430` | green-3 | TA-RED-009 + 메시지 | `test_none_grid_message_exact_match_...`, `test_none_grid_returns_error_response_struct_type` |
| `d0fe1e2` | green-4 | TA-RED-007~008 | `test_none_grid_resolve_called_zero_times_...`, `test_none_grid_resolve_mock_invocation_...` |

메타 테스트 `test_scope_excludes_...` (R-05-05)는 프로덕션 코드 없이 PASS — 별도 GREEN 커밋 없음.

### 진행률

| 구분 | 설계 묶음 | GREEN 커밋 | 테스트 수 |
|------|:--------:|:----------:|:---------:|
| Report/05 — AC-FR-01-01 | 5 / 7 | **4** | 9 / 11 |
| Report/09 — Dual-Track | 0 / 12 | 0 | 0 / 24 |
| **합계** | **5 / 19** | **4** | **9 / 35** |

*11·35: test_plan 갭(TA-RED-005·006·010) RED 미작성 2묶음 포함.*

### 회귀 기준선 (항상 GREEN 유지)

```powershell
python -m pytest tests/boundary/test_ac_fr_01_01_matrix_size.py tests/control/test_ac_fr_01_01_domain_isolation.py -q
# → 9 passed (2026-05-29 기준)
```

### Report/05 — AC-FR-01-01 RED 묶음 (U-IN-01~02 대응)

| 묶음 ID | test_plan | 테스트 수 | RED | GREEN | 검증 내용 |
|---------|-----------|:---------:|:---:|:---:|-----------|
| **R-05-01** | TA-RED-001 | 1 | ✅ | ✅ | `grid=None` → `INVALID_SIZE` |
| **R-05-02** | TA-RED-002~004 | 3 | ✅ | ✅ | `[]`, `[[]]*4`, 3×4 → `INVALID_SIZE` |
| **R-05-03** | TA-RED-009 + 메시지 | 2 | ✅ | ✅ | `ErrorResponse` 타입, message 바이트 동일 |
| **R-05-04** | TA-RED-007~008 | 2 | ✅ | ✅ | 크기 오류 시 `solver.resolve` 0회 |
| **R-05-05** | (메타) | 1 | ✅ | ✅ | AC-FR-01-02~05·FR-02~05 범위 제외 확인 |
| R-05-GAP-A | TA-RED-005~006 | — | ❌ | ❌ | 4×3, 5×5 — **RED 테스트 미작성** |
| R-05-GAP-B | TA-RED-010 | — | ❌ | ❌ | 결정성(NFR-03) — **RED 테스트 미작성** |

**구현 산출물**: `boundary/validator.py`, `boundary/schemas.py`, `control/resolver.py`, `entity/solver.py` (스텁) — [Report/10](Report/10.%20MagicSquare_AC_FR_01_01_GREEN_Test_Implementation_Report.md)  
**GUI 산출물**: `boundary/screen/`, `control/factory.py`, `requirements-gui.txt` — [Report/12](Report/12.%20MagicSquare_M1_GUI_PyQt_Implementation_Report.md)

### Report/09 — Dual-Track RED 묶음 (Logic + UI)

Track B(Logic)를 먼저, FR-05에서 U-OUT과 짝을 맞춥니다. 각 행 = **RED 1묶음 → GREEN 1커밋** 목표.

| 묶음 ID | Test ID | Track | FR | 테스트 수 | RED | GREEN | 다음 GREEN 커밋 메시지 예 |
|---------|---------|:-----:|:--:|:---------:|:---:|:---:|---------------------------|
| **R-09-B01** | D-LOC-01 | B | FR-02 | 1 | ✅ | ✅ | `feat(green): D-LOC-01 blank coords G1` |
| **R-09-B02** | D-MIS-01 | B | FR-03 | 1 | ✅ | ✅ | `feat(green): D-MIS-01 missing numbers G1` |
| **R-09-B03** | D-VAL-01 | B | FR-04 | 1 | ✅ | ✅ | `feat(green): D-VAL-01 is_magic_square true` |
| **R-09-B04** | D-VAL-02~06 | B | FR-04 | 5 | ✅ | ✅ | `feat(green): D-VAL-02~06 is_magic_square false cases` |
| **R-09-B05** | D-SOL-01 | B | FR-05 | 1 | ✅ | ✅ | `feat(green): D-SOL-01 G1_SOL small-first` |
| **R-09-B06** | D-SOL-02 | B | FR-05 | 1 | ✅ | ✅ | `feat(green): D-SOL-02 G2 reverse` |
| **R-09-B07** | D-SOL-03 | B | FR-05 | 1 | ✅ | ✅ | `feat(green): D-SOL-03 G3 unsolvable` |
| **R-09-B08** | D-SOL-04 | B | FR-05 | 1 | ✅ | ✅ | `feat(green): D-SOL-04 output length and 1-index` |
| **R-09-A01** | U-IN-04 | A | FR-01 | 1 | ✅ | ✅ | `feat(green): U-IN-04 INVALID_BLANK_COUNT` |
| **R-09-A02** | U-IN-05 | A | FR-01 | 1 | ✅ | ✅ | `feat(green): U-IN-05 VALUE_OUT_OF_RANGE` |
| **R-09-A03** | U-IN-06 | A | FR-01 | 1 | ✅ | ✅ | `feat(green): U-IN-06 DUPLICATE_NON_ZERO_VALUE` |
| **R-09-A04** | U-IN-07 | A | FR-01 | 1 | ✅ | ✅ | `feat(green): U-IN-07 no blanks` |
| **R-09-A05** | U-IN-08 | A | FR-01 | 1 | ✅ | ✅ | `feat(green): U-IN-08 G1 valid input pass` |
| **R-09-A06** | U-FLOW-02 | A | FR-01 | 4 | ✅ | ✅ | `feat(green): U-FLOW-02 invalid execute 0 calls` |
| **R-09-A07** | U-OUT-01 | A | FR-05 | 1 | ✅ | ✅ | `feat(green): U-OUT-01 success envelope` |
| **R-09-A08** | U-OUT-02 | A | FR-05 | 1 | ✅ | ✅ | `feat(green): U-OUT-02 1-index coords` |
| **R-09-A09** | U-OUT-03 | A | FR-05 | 1 | ✅ | ✅ | `feat(green): U-OUT-03 G3 failure envelope` |

**범례**: ✅ 완료 · 🟡 RED 스켈레톤(`pytest.fail`)만 존재 · ❌ 미작성 또는 GREEN 미착수

**Report/09 상태 (2026-05-29):** 스켈레톤 16건 **GREEN 완료** — `pytest -q` **70 passed**. 상세: [Report/16](Report/16.%20MagicSquare_Coverage_Gate_GREEN_QA_Report.md).

**Report/06 설계 대비 갭**

| Test ID | 비고 |
|---------|------|
| U-IN-01, U-IN-02 | Report/05 `test_ac_fr_01_01_*`로 **대체·GREEN 완료** (`INVALID_SIZE` 계약) |
| U-IN-03 | 빈칸 1개 → E002 — **RED·GREEN 모두 미작성** |
| G3 격자 | ✅ GM-TC-05 SSOT (`tests/entity/grids.py` `GRID_G3`) |
| D-SOL-01 기대값 | Report/06 `[2,2,7,3,3,10]` → GM-TC-01 `[1,2,2,1,3,3]` (`GRID_G1_SOL`) |

### 작업 진행 목표 (마일스톤)

| 마일스톤 | 목표 | 상태 |
|----------|------|------|
| **M1** | AC-FR-01-01 크기 검증 RED→GREEN (Report/05, **4 GREEN 커밋**) | ✅ 완료 (9건) |
| **M1-GUI** | Boundary 크기 오류 GUI 표시 (`boundary/screen/`) | ✅ 셸 + presenter/GUI SSOT pytest |
| **M2** | Track B Logic GREEN — D-LOC → D-MIS → D-VAL → D-SOL | ✅ 완료 ([Report/16](Report/16.%20MagicSquare_Coverage_Gate_GREEN_QA_Report.md)) |
| **M3** | Track A UI GREEN — U-IN-04~08, U-FLOW-02 (short-circuit) | ✅ 완료 |
| **M4** | FR-05 Dual-Track — U-OUT-01~03 (D-SOL 이후) | ✅ 완료 |
| **M5** | test_plan 갭 — 4×3·5×5·결정성 RED+GREEN | ⏳ |
| **M6** | REFACTOR 시리즈 — [REFACTOR To-Do](#refactor-to-do-리스트) (ECB·SRP·테스트 3그룹) · **GREEN 커밋과 분리** | ⏳ P0 완료 · P1 잔존 |
| **M7** | 전체 회귀 + 커버리지 (Boundary/Control ≥85%, Entity ≥95%) | ✅ **부분** — Entity 96.8% · Control 100% · Boundary core 95% · 전역 55% |

### 커버리지 목표

- [x] Domain Logic: 95%+ (`pytest --cov=entity`) — **96.8%**
- [x] Boundary Layer: 85%+ — 계약 core **~98%** *(screen 제외)*
- [x] Control Layer: 85%+ — **100%**
- [x] AC-FR-01-01 회귀 9건 상시 GREEN

### 결함 목록 연결

- [x] defect_list.md 생성 및 RED 단계 결함 기록
- [x] Report/05 DEF-001~009 — AC-FR-01-01 GREEN으로 해소 (문서 갱신 권장)
- [x] Report/09 스켈레톤 16건 GREEN — **70 passed** ([Report/16](Report/16.%20MagicSquare_Coverage_Gate_GREEN_QA_Report.md))

---

## 커버리지 Gate To-Do

> **SSOT:** [Report/16](Report/16.%20MagicSquare_Coverage_Gate_GREEN_QA_Report.md) · QA 커버리지 분석 (2026-05-29) · `test_plan.md` §7 · PRD NFR-01~03  
> **회귀 안전망 (매 항목 완료 후):** **70 passed** + Golden Master 17  
> **측정 경로:** `entity/`, `boundary/`, `control/` (repo 루트 — `src/` 없음)  
> **실행 순서:** ① → ② → ③ → ④ → ⑤ → ⑥ (의존성 순)

### ① G3 unsolvable 격자 SSOT (선행)

- [x] `tests/entity/grids.py` — `GRID_G3` = GM-TC-05 (양 조합 실패 격자)
- [x] `GRID_G1_SOL` 추가 — GM-TC-01 small-first 성공 격자

> Report/06 G1은 D-LOC/D-MIS/U-IN-08용 유지. D-SOL-01은 `GRID_G1_SOL` + `[1,2,2,1,3,3]`.

### ② D-SOL GREEN + Domain ≥ 95% gap (Track B)

- [x] `test_d_sol_01_04_solution.py` — D-SOL-01~04 (4건)
- [ ] `test_d_val_01_06_magic_square.py` — D-VAL 대각선 L39/L42 *(4×4 row·col=34이면 대각도 34 — 격리 불가)*
- [x] `test_d_loc_01_blank_coords.py` — D-LOC-02
- [x] `test_d_mis_01_missing_numbers.py` — D-MIS-02

**Gate:** entity **96.8%** ✅

### ③ U-IN GREEN (Track A — FR-01)

- [x] `boundary/input_validator.py` — `VALUE_OUT_OF_RANGE`
- [x] `test_u_in_04_08_input_validation.py` — U-IN-04~08 (5건)

### ④ U-FLOW GREEN (Track A — AC-FR01-05)

- [x] `test_u_flow_02_execute_zero_calls.py` — U-FLOW-02 (4건)

### ⑤ U-OUT GREEN (Track A — FR-05)

- [x] `test_u_out_01_03_output_contract.py` — U-OUT-01~03 (3건)

### ⑥ Gate 재검증 + GUI 계약 (Report/12)

- [x] `python -m pytest -q` → **70 passed, 0 failed**
- [x] Entity **96.8%** · Control **100%** · Boundary 계약 core **~98%**
- [x] Golden Master 17 + GM-1 PASS
- [x] `test_gui_invalid_size_message.py` · `test_screen_presenter.py` (PyQt 불필요)
- [ ] `main_window.py` PyQt 통합 테스트 *(PyQt6 + `pytest-qt` 필요, CI optional)*
- [ ] 전역 ≥ 80% *(screen/main_window 188 stmts — PyQt 환경 또는 omit)*

---

## 다음 단계 (권장 실행 순서)

1. ~~**G3 unsolvable 격자 확정**~~ → [커버리지 Gate To-Do ①](#-g3-unsolvable-격자-ssot-선행)
2. ~~**`test_gui_*.py` RED**~~ — ✅ `test_gui_invalid_size_message.py` + `test_screen_presenter.py` (PyQt 불필요)
3. ~~**R-09-B01** D-LOC-01~~ — ✅ 완료
4. ~~R-09-B04 → B05~B08 Logic GREEN~~ → [Gate To-Do ②③](#-d-sol-green--domain--95-gap-track-b)
5. ~~R-09-A01~A06 FR-01 UI 잔여~~ → [Gate To-Do ③④](#-u-in-green-track-a--fr-01)
6. ~~R-09-A07~A09 FR-05 출력 계약~~ → [Gate To-Do ⑤](#-u-out-green-track-a--fr-05-③④-이후)
7. R-05-GAP-A/B — 4×3·5×5·결정성 RED 작성 후 GREEN
8. REFACTOR 전용 커밋 (API `INVALID_SIZE` ↔ `E001~E005` 통합 등)
9. Data / Integration RED — 별도 스프린트

---

## Definition of Done (구현 단계)

- [x] 입력/출력 고정 계약 테스트가 모두 통과한다. *(70 passed, U-IN-03·GAP 제외)*
- [x] Domain/UI Track B·A RED 스켈레톤이 GREEN이다. *(Report/09 16건)*
- [ ] Domain/UI/Data/Integration **전체** 그린 *(U-IN-03, R-05-GAP, PyQt main_window 잔존)*
- [ ] 리팩토링 후에도 계약 형식과 오류 코드가 유지된다.
- [ ] 기존 테스트 삭제 없이 회귀 테스트 세트가 유지된다.
- [x] README/Report와 실제 테스트 규칙이 불일치하지 않는다. *(Report/16·G1_SOL SSOT 반영)*

---

## 운영 원칙 (요약)

- 도메인 규칙보다 구현 편의가 우선될 수 없다.
- 계약(입력/출력/오류)을 테스트보다 늦게 바꾸지 않는다.
- 테스트가 없는 리팩토링은 수행하지 않는다.
- 레이어 침범(예: Domain의 UI/Data 구현 의존)을 허용하지 않는다.
- 실패를 숨기지 않고, 코드/메시지로 명시한다.

---

## 문서 이력

| 버전 | 날짜 | 내용 |
|------|------|------|
| 1.0 | 2026-05-28 | README 최초 작성 (STEP 1~5 보고서·프롬프트 기반) |
| 1.1 | 2026-05-28 | 프로젝트 정의/목적/목표 고도화 + 마방진=도메인, 목표=TDD 구현 훈련 방향 통합 + RED-GREEN-REFACTOR 운영 규칙/고정 계약/DoD/불변조건 정합성 반영 |
| 1.2 | 2026-05-28 | Report/Prompt 문서 목록 최신화 (03, 04 추가) + Level 1~5 통합 검증 보고서 및 Transcript 링크 반영 |
| 1.3 | 2026-05-29 | AC-FR-01-01 RED 테스트 보고서(05)·Transcript(05)·test_plan.md 링크 반영 |
| 1.4 | 2026-05-29 | FR-01~FR-05 Dual-Track RED 설계 보고서(06)·Transcript(06) 링크 반영 |
| 1.5 | 2026-05-29 | Dual-Track RED 스켈레톤 구현 보고서(09)·Transcript(07) 링크 반영 |
| 1.6 | 2026-05-29 | AC-FR-01-01 GREEN(Report/10) 반영 · RED 묶음별 진행 현황·마일스톤·저장소 구조 갱신 |
| 1.7 | 2026-05-29 | GREEN 4커밋 이력·설계/커밋 묶음 구분·로컬 실행·GUI 검토 섹션 추가 |
| 1.8 | 2026-05-29 | Report/11·Prompt/11 링크 반영 (분할 GREEN·TDD 진행 세션) |
| 1.9 | 2026-05-29 | M1-GUI PyQt6 셸 구현·GUI 실행 섹션·Report/12·Prompt/12·`requirements-gui.txt` 반영 |
| 1.10 | 2026-05-29 | Golden Master 회귀 안전장치(GM-01~10) 섹션 추가 — `test_golden_master_magic_square.py`·`golden_master_expected.txt` |
| 1.11 | 2026-05-29 | REFACTOR To-Do 리스트 추가 — Report/14 기반 3그룹(A ECB · B SRP/계약 · C 테스트) 체크리스트 |
| 1.12 | 2026-05-29 | 그룹 C P0 완료(수집 0건)·P1 Track B 8건 GREEN — `ui_boundary`, `solve_partial`, `tests/entity/grids.py` |
| 1.13 | 2026-05-29 | ECB 리팩터(9d3250b)·size 검증 Result Type(2번째 커밋) — pipeline boundary 이동, Screen→UIBoundary |
| 1.14 | 2026-05-29 | Report/15·Prompt/15 — REFACTOR P0 구현 보고서·Transcript export |
| 1.15 | 2026-05-29 | Report/16·Prompt/16 — 커버리지 Gate GREEN · QA 분석 · RED 16→0 · 70 passed · M2~M4·M7 Gate 갱신 |

---

*본 README는 학습 방향과 TDD 진행 현황의 SSOT입니다. **설계 묶음**은 test_plan 추적용, **커밋 묶음**은 git log(`bc022cb`~`d0fe1e2`) 기준입니다. 최신 회귀: `python -m pytest -q` → **70 passed** (Report/16). GUI 실행: `python -m boundary.screen.app` (PyQt6, `requirements-gui.txt`).*
