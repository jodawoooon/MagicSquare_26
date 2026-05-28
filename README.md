# MagicSquare_xxx

4×4 **마방진(Magic Square)** 을 도메인으로, **TDD 구현 역량**을 훈련하는 학습 프로젝트입니다.  
핵심은 정답 알고리즘을 빨리 만드는 것이 아니라, **계약 고정 -> 테스트 우선 -> 리팩토링**을 반복하며 안정적으로 개발하는 것입니다.

| 항목 | 내용 |
|------|------|
| **현재 단계** | 문제 정의 완료 + TDD 설계 문서화 완료 |
| **1차 범위** | 4×4 입력 계약 기반 **해결 결과 산출** |
| **훈련 초점** | Domain 중심 설계 + Contract-first 테스트 |
| **상태** | 구현 코드 없이 설계/계약/테스트 계획 완료 → TDD 구현 착수 준비 |

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
- 그래픽 UI 화면 구현
- 원격 DB/네트워크 영속성
- 3×3, 5×5 등 다른 차수 일반화

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
├── Report/
│   └── 01. 4x4_MagicSquare_Problem_Definition_Report.md
│   └── 02. 4x4_MagicSquare_Dual-Track_TDD_CleanArchitecture_Design_Report.md
└── Prompt/
    └── 01. 4x4_MagicSquare_Problem_Definition_Report_Prompt.md
    └── 02. MagicSquare_4x4_TDD_Interactive_Prompt_Transcript.md
```

| 경로 | 설명 |
|------|------|
| [Report/01. 4x4_MagicSquare_Problem_Definition_Report.md](Report/01.%204x4_MagicSquare_Problem_Definition_Report.md) | STEP 1~5 **통합 보고서** (목차·상세 분석·합의 체크리스트) |
| [Report/02. 4x4_MagicSquare_Dual-Track_TDD_CleanArchitecture_Design_Report.md](Report/02.%204x4_MagicSquare_Dual-Track_TDD_CleanArchitecture_Design_Report.md) | Dual-Track UI+Logic TDD + Clean Architecture **설계 보고서** |
| [Prompt/01. 4x4_MagicSquare_Problem_Definition_Report_Prompt.md](Prompt/01.%204x4_MagicSquare_Problem_Definition_Report_Prompt.md) | 동일 워크플로 **재실행용** 대화형 프롬프트 transcript |
| [Prompt/02. MagicSquare_4x4_TDD_Interactive_Prompt_Transcript.md](Prompt/02.%20MagicSquare_4x4_TDD_Interactive_Prompt_Transcript.md) | 현재 요구 반영 **대화형 실행 프롬프트 export** |

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
- 커밋 단위는 `RED -> GREEN -> REFACTOR` 흐름을 추적 가능하게 유지한다.
- 계약 변경이 필요한 경우, 먼저 테스트/문서를 갱신한 뒤 구현을 수정한다.

---

## 다음 단계 (권장 실행 순서)

현재 기준의 권장 실행 순서는 다음과 같습니다.

1. Domain RED: 입력 계약/불변조건/순서 정책 테스트 작성  
2. Domain GREEN/REFACTOR: 최소 구현 후 구조 정리  
3. UI Boundary RED: 입력 오류/출력 포맷/오류 메시지 테스트 작성  
4. Data RED: InMemory 저장/로드 정합성 테스트 작성  
5. Integration RED: UI -> Domain -> Data 경로 테스트 작성  
6. 각 레이어별 GREEN/REFACTOR 반복 후 전체 회귀 테스트 고정

---

## Definition of Done (구현 단계)

- [ ] 입력/출력 고정 계약 테스트가 모두 통과한다.
- [ ] Domain/UI/Data/Integration 테스트가 모두 그린이다.
- [ ] 리팩토링 후에도 계약 형식과 오류 코드가 유지된다.
- [ ] 기존 테스트 삭제 없이 회귀 테스트 세트가 유지된다.
- [ ] README/Report와 실제 테스트 규칙이 불일치하지 않는다.

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

---

*본 README는 학습 방향과 실행 순서를 정의합니다. 실제 구현 코드는 TDD 사이클에 따라 별도 단계에서 추가됩니다.*
