# Quantum Security Lab

A hands-on learning and engineering project for building strong skills in:

- Machine learning
- Data science
- Optimisation
- Software engineering
- Full-stack development
- Edge/embedded computing
- Quantum computing and quantum cryptography
- Cybersecurity and post-quantum cryptography

The goal is **not** to build a giant quantum simulator. Quantum technology is the domain; the main curriculum is real software, data, ML, optimisation, systems and security engineering.

---

## 1. Project Vision

Build a full-stack **Quantum Security Lab** that can run experiments involving quantum-security concepts, collect and analyse security telemetry, detect attacks/anomalies with ML, optimise security configurations, and eventually run parts of the system on Raspberry Pi and Jetson Nano hardware.

The long-term system should look roughly like:

```text
                    ┌──────────────────────────┐
                    │       Web Dashboard      │
                    │      React / Next.js     │
                    └────────────┬─────────────┘
                                 │
                    ┌────────────▼─────────────┐
                    │       FastAPI Backend     │
                    └───────┬─────────┬─────────┘
                            │         │
                 ┌──────────▼───┐ ┌──▼────────────┐
                 │ PostgreSQL   │ │ ML / Optimiser │
                 │ Experiment   │ │    Services    │
                 │ Data         │ └──────┬─────────┘
                 └──────────────┘        │
                                         │
                              ┌──────────▼──────────┐
                              │ Quantum Security    │
                              │ Experiments         │
                              │ BB84 / PQC / etc.   │
                              └──────────┬──────────┘
                                         │
                         ┌───────────────┴───────────────┐
                         │                               │
                   ┌─────▼─────┐                   ┌─────▼─────┐
                   │ Raspberry │                   │ Jetson    │
                   │ Pi Alice  │                   │ Nano      │
                   │ / Bob     │                   │ Edge ML   │
                   └───────────┘                   └───────────┘
```

---

# 2. Learning Priorities

The project has four primary learning tracks.

### Primary

1. **Data science**
   - NumPy
   - pandas
   - statistics
   - visualisation
   - experimental analysis
   - feature engineering

2. **Machine learning**
   - supervised learning
   - classification
   - anomaly detection
   - model evaluation
   - feature importance
   - neural networks
   - deployment

3. **Optimisation**
   - objective functions
   - constraints
   - search
   - grid/random search
   - Bayesian optimisation
   - evolutionary methods
   - multi-objective optimisation

4. **Software engineering**
   - Python architecture
   - testing
   - APIs
   - databases
   - Docker
   - Git
   - CI/CD
   - distributed systems

### Secondary

- AWS/cloud infrastructure
- Raspberry Pi
- Jetson Nano
- Frontend development
- DevOps
- Production deployment

### Frontier-tech domain

- Quantum computing
- Quantum cryptography
- Quantum attacks/threat models
- Post-quantum cryptography
- Cryptographic engineering

---

# 3. Roadmap

## Phase 0 — Project Foundation

**Goal:** Establish a clean Python project and learn the workflow.

- [ ] Create Git repository
- [ ] Set up Python environment
- [ ] Set up project structure
- [ ] Add `pytest`
- [ ] Add formatting/linting
- [ ] Create first unit tests
- [ ] Learn Git workflow
- [ ] Create a basic experiment runner

### Concepts

- Python packages
- virtual environments
- modules
- classes/functions
- testing
- Git
- reproducibility

---

# Phase 1 — Quantum Foundations

**Goal:** Understand enough quantum computing to work with quantum-security concepts.

Do not try to build a full quantum simulator.

Implement only the concepts we need.

- [ ] Represent a qubit
- [ ] Understand superposition
- [ ] Implement basic gates
- [ ] Implement measurement
- [ ] Understand probability amplitudes
- [ ] Understand computational vs alternative bases
- [ ] Write small experiments
- [ ] Visualise measurement statistics

### Key question

> How does measuring a quantum system affect the information we can obtain from it?

---

# Phase 2 — BB84

**Goal:** Build the first genuinely interesting system.

Implement the **BB84 quantum key distribution protocol**.

- [ ] Alice generates random bits
- [ ] Alice chooses random bases
- [ ] Alice encodes states
- [ ] Bob chooses random measurement bases
- [ ] Bob measures
- [ ] Alice and Bob compare bases
- [ ] Generate the sifted key
- [ ] Calculate QBER
- [ ] Simulate/noise model
- [ ] Add Eve
- [ ] Measure the effect of interception

### First major experiment

Run thousands of BB84 experiments and investigate:

```text
Eve interception probability
            ↓
          QBER
            ↓
     probability of
      detecting Eve
```

### Questions to investigate

- How does Eve change QBER?
- How many bits are required before an attack becomes statistically obvious?
- How does noise affect detection?
- Can we distinguish noise from an attack?

This is where the data-science side begins.

---

# Phase 3 — Experiment & Data Platform

**Goal:** Turn experiments into a real dataset.

Instead of throwing experiment results away, store them.

Collect features such as:

- QBER
- key length
- sifted key length
- transmission errors
- noise level
- Eve probability
- measurement statistics
- latency
- packet loss
- device information
- experiment configuration

### Build

- [ ] Experiment runner
- [ ] Dataset generation pipeline
- [ ] pandas analysis notebooks
- [ ] PostgreSQL database
- [ ] Experiment metadata
- [ ] Reproducible experiment IDs
- [ ] Statistical summaries
- [ ] Visualisation dashboard

### Data-science questions

- What variables are most predictive of an attack?
- What is normal system behaviour?
- How much data is needed to identify abnormal behaviour?
- Which measurements contain useful information?

---

# Phase 4 — ML Cybersecurity

**Goal:** Use machine learning to identify suspicious behaviour.

Start simple.

### Models

- [ ] Logistic regression
- [ ] Decision tree
- [ ] Random forest
- [ ] Gradient boosting
- [ ] Neural network
- [ ] Anomaly detection

### Tasks

Create datasets containing:

```text
NORMAL
NOISY
EVE ATTACK
NETWORK ANOMALY
DEVICE ANOMALY
```

Train models to classify them.

### Learn

- train/test split
- cross-validation
- precision
- recall
- F1 score
- ROC/AUC
- class imbalance
- feature engineering
- model interpretation
- false positives vs false negatives

### Core question

> Can we detect a quantum-security attack from the observable behaviour of the system?

---

# Phase 5 — Raspberry Pi Distributed System

**Goal:** Move from a notebook into physical computing.

Use two Raspberry Pis as distributed endpoints.

```text
Raspberry Pi A
     │
     │ telemetry / experiment
     │
     ▼
Raspberry Pi B
     │
     ▼
Security backend
```

Possible roles:

### Pi A — Alice

- experiment generation
- key generation
- telemetry

### Pi B — Bob

- measurements
- verification
- telemetry

### Learn

- networking
- REST APIs
- device identity
- authentication
- secure communication
- latency
- packet loss
- distributed systems
- system monitoring

---

# Phase 6 — Jetson Nano Edge ML

**Goal:** Run security intelligence at the edge.

The Jetson becomes the local security/ML node.

```text
Raspberry Pis
      │
      ▼
  telemetry
      │
      ▼
 Jetson Nano
      │
      ├── feature extraction
      ├── ML inference
      └── anomaly detection
```

### Tasks

- [ ] Deploy trained model
- [ ] Run inference locally
- [ ] Measure inference latency
- [ ] Measure CPU/GPU utilisation
- [ ] Compare edge vs cloud inference
- [ ] Build alerting
- [ ] Investigate model size/performance tradeoffs

### Core question

> When should security intelligence run locally instead of in the cloud?

---

# Phase 7 — Optimisation Engine

**Goal:** Make optimisation a central part of the system.

Define a configurable security system.

Example:

```text
Security
   +
Detection accuracy
   -
Latency
   -
Compute cost
   -
Energy usage
```

The optimiser searches for the best configuration.

Possible parameters:

- model choice
- model threshold
- key length
- detection threshold
- sampling frequency
- telemetry frequency
- edge/cloud inference
- encryption configuration
- compute allocation

### Start with

- [ ] Grid search
- [ ] Random search
- [ ] Constraint optimisation

Then progress to:

- [ ] Bayesian optimisation
- [ ] Evolutionary optimisation
- [ ] Multi-objective optimisation

### Core question

> What configuration gives the best security while satisfying latency, compute and energy constraints?

This is where the optimisation skills connect directly to the rest of the project.

---

# Phase 8 — Post-Quantum Cryptography

**Goal:** Connect quantum threats to practical cybersecurity.

Study and benchmark classical and post-quantum approaches.

Compare things such as:

- RSA
- ECC
- modern post-quantum algorithms
- key sizes
- signature sizes
- encryption/decryption performance
- memory usage
- CPU usage
- network overhead

Run the benchmarks on:

- laptop
- Raspberry Pi
- Jetson Nano

### Questions

- How expensive is post-quantum security on edge hardware?
- Which algorithms perform best on constrained devices?
- What trade-offs exist between security, performance and bandwidth?
- Can optimisation select an appropriate cryptographic configuration?

---

# Phase 9 — Full-Stack Quantum Security Lab

**Goal:** Turn the project into a real application.

## Frontend

Possible stack:

- React
- Next.js
- TypeScript
- charts/visualisation

Dashboard sections:

### Experiments

Run and inspect quantum-security experiments.

### Security

View:

- QBER
- attack probability
- anomaly score
- alerts

### ML

View:

- datasets
- models
- metrics
- feature importance

### Optimisation

Configure:

- objective
- constraints
- candidate configurations
- optimisation results

### Hardware

Monitor:

- Raspberry Pis
- Jetson
- latency
- CPU
- memory
- network health

### Cryptography

Compare:

- classical cryptography
- post-quantum cryptography
- hardware benchmarks

---

# Phase 10 — Cloud / AWS

AWS should be introduced when the system actually needs it.

Potential architecture:

```text
Local hardware
      │
      ▼
API / ingestion
      │
      ▼
AWS
 ├── compute
 ├── database
 ├── model inference
 ├── storage
 └── monitoring
```

Possible services to learn organically:

- Lambda
- API Gateway
- S3
- DynamoDB or PostgreSQL
- CloudWatch
- ECS/Fargate
- IAM
- EventBridge

The goal is not to memorise AWS services.

The goal is:

> Build a system, encounter a deployment problem, then learn the AWS service that solves it.

---

# 4. Suggested Technology Stack

## Python

Core language.

```text
NumPy
pandas
SciPy
scikit-learn
PyTorch
pytest
```

Later:

```text
Qiskit
optimisation libraries
cryptography/PQC libraries
```

## Backend

```text
FastAPI
PostgreSQL
SQLAlchemy
```

## Frontend

```text
React / Next.js
TypeScript
```

## Infrastructure

```text
Docker
Git
GitHub Actions
AWS
```

## Hardware

```text
Raspberry Pi
Jetson Nano
```

---

# 5. Repository Structure

A starting structure:

```text
quantum-security-lab/
│
├── README.md
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml
│
├── src/
│   ├── quantum/
│   │   ├── qubit.py
│   │   ├── gates.py
│   │   └── measurement.py
│   │
│   ├── crypto/
│   │   ├── bb84.py
│   │   └── pqc.py
│   │
│   ├── experiments/
│   │   ├── runner.py
│   │   └── scenarios.py
│   │
│   ├── ml/
│   │   ├── features.py
│   │   ├── train.py
│   │   └── inference.py
│   │
│   ├── optimisation/
│   │   ├── objectives.py
│   │   └── optimiser.py
│   │
│   └── api/
│       └── main.py
│
├── notebooks/
│   ├── 01_quantum_basics.ipynb
│   ├── 02_bb84.ipynb
│   └── 03_eve_analysis.ipynb
│
├── tests/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── frontend/
│
└── docs/
```

This structure will evolve. Don't spend days designing it upfront.

---

# 6. Development Philosophy

## Build → Measure → Learn → Improve

Every stage should answer a real question.

Instead of:

> "I need to learn random forests."

Use:

> "I need to detect attacks, and I wonder whether a random forest can do it."

Instead of:

> "I need to learn Bayesian optimisation."

Use:

> "I need to find the best security configuration without testing thousands of possibilities."

Instead of:

> "I need to learn AWS Lambda."

Use:

> "My experiment runner needs scalable asynchronous execution."

The technology should be pulled into the project by a real problem.

---

# 7. What NOT to Do

### Don't build a huge quantum simulator

We only need enough quantum mechanics to understand and experiment with the security concepts.

### Don't start with AWS

Get the local system working first.

### Don't start with neural networks

Simple models are better for understanding the data.

### Don't optimise before defining the objective

First understand what you're optimising.

### Don't build the entire SaaS application immediately

Build the smallest useful system, then expand it.

---

# 8. Milestones

## Milestone 1 — BB84

**Outcome:** Working BB84 implementation.

```text
Alice → Quantum Channel → Bob
             ↑
            Eve
```

Generate thousands of experiments and analyse QBER.

---

## Milestone 2 — Security Dataset

**Outcome:** A real dataset describing normal and attacked experiments.

---

## Milestone 3 — Attack Detection

**Outcome:** ML model capable of identifying suspicious experiments.

---

## Milestone 4 — Physical Network

**Outcome:** Raspberry Pis communicating with the security platform.

---

## Milestone 5 — Edge AI

**Outcome:** Jetson Nano running security inference locally.

---

## Milestone 6 — Optimisation

**Outcome:** Optimiser automatically selecting security configurations.

---

## Milestone 7 — PQC Benchmarking

**Outcome:** Practical comparison of cryptographic approaches on constrained hardware.

---

## Milestone 8 — Full-Stack Platform

**Outcome:** Web dashboard for running, analysing and optimising experiments.

---

# 9. First Task

Do **only this** first.

## Build BB84 in Python.

The first version does not need:

- a frontend
- AWS
- PostgreSQL
- Raspberry Pi
- Jetson
- machine learning
- Docker

Just Python.

### First target

Create:

```text
src/
└── crypto/
    └── bb84.py
```

Implement:

```text
Alice
  ↓
random bits
  ↓
random bases
  ↓
encoding
  ↓
quantum channel
  ↓
Bob
  ↓
random measurement bases
  ↓
measurement
  ↓
basis reconciliation
  ↓
sifted key
  ↓
QBER
```

Then add Eve.

Finally run thousands of experiments and plot:

```text
Eve interception probability
             vs
            QBER
```

That graph is the first real scientific result of the project.

---

# 10. The Long-Term Goal

By the end, this should not feel like a collection of tutorials.

It should feel like a real engineering/research platform:

> **A full-stack quantum-security experimentation platform that uses data science, machine learning and optimisation to investigate attacks, security configurations and cryptographic trade-offs across cloud and edge hardware.**

The quantum technology makes the project interesting.

The **ML, optimisation, data and software engineering** are what make it valuable as a learning project.

---

## Current Status

**Phase:** 0 — Project Foundation

**Next milestone:** Implement BB84.

**Primary learning objective:** Learn by building.

**Rule:** Keep the system small enough that you understand every layer before adding the next one.
