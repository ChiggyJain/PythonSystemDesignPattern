# PythonSystemDesignPattern

An **industry-grade FastAPI backend project** demonstrating how real-world ERP / SaaS systems are designed using **clean system design patterns**, async-first architecture, and production hardening techniques.

This project is **not tutorial-style CRUD**. It focuses on **how senior backend engineers structure systems** that are scalable, testable, and resilient.

---

## 🚀 Tech Stack

- **Python 3.12**
- **FastAPI (Async)**
- **SQLAlchemy Async + MySQL**
- **Redis (conceptual)**
- **Queue-based async processing (Kafka / Celery – conceptual)**
- **Async-first design (no blocking I/O)**

---

## 🧠 System Design Patterns Implemented

### 1️⃣ Layered Architecture
Clear separation of:
- API Layer (HTTP & validation)
- Service Layer (business orchestration)
- Repository Layer (data access)
- Domain Models
- Infrastructure (DB, Queue, External APIs)

---

### 2️⃣ Dependency Injection (FastAPI Way)
- Clean object lifecycle management using `Depends`
- Loose coupling between API, services, repositories
- Easy mocking & testing

---

### 3️⃣ Repository vs Service Pattern
- Repository handles **only data access**
- Service handles **business rules & workflows**
- Prevents God objects and tight coupling

---

### 4️⃣ Factory Pattern
- Centralized object creation
- Eliminates `if/else` explosions
- Enables plug-and-play implementations

---

### 5️⃣ Strategy Pattern
- Encapsulates business algorithms
- Dynamic runtime behavior selection
- Ideal for pricing, rules, discounts, routing

---

### 6️⃣ Adapter Pattern (External APIs)
- Clean integration with external systems (Email, SMS, etc.)
- Vendor-specific logic isolated from core business
- Core system remains stable when vendors change

---

### 7️⃣ Facade Pattern
- Provides a **single entry point** for complex workflows
- Hides orchestration of DB, queue, strategies, adapters
- Keeps APIs extremely clean and readable

---

### 8️⃣ Retry Pattern
- Handles transient external failures safely
- Async retry with backoff
- Prevents unnecessary request failures

---

### 9️⃣ Circuit Breaker Pattern
- Prevents cascading failures
- Fast-fails when external services are unhealthy
- Automatically recovers after cooldown

---

## 🔁 End-to-End ERP Flow Implemented

**Example: Exam Fee Submission**

1. API receives request
2. Fee stored in MySQL (async)
3. Event published to queue
4. Worker processes side-effects
5. Notification sent via external adapter
6. External failures isolated with retry + circuit breaker

This ensures:
- Fast API responses
- Strong data consistency
- Failure isolation
- Horizontal scalability

---

## 📁 Project Structure (Simplified)

```
app/
├── api/              # FastAPI routes
├── facades/          # Workflow orchestration
├── services/         # Business logic
├── repositories/     # Data access layer
├── strategies/       # Business rules
├── factories/        # Object creation
├── adapters/         # External integrations
├── ports/            # System-owned interfaces
├── core/             # DB, retry, circuit breaker
└── queue/            # Async event publishing
```

---

## 🎯 Why This Project Matters

- Mirrors **real enterprise backend design**
- Interview-ready system design explanations
- Demonstrates senior-level thinking
- Clean separation of concerns
- Production-hardening patterns included

---

## 📌 Ideal For

- Backend engineers transitioning to senior roles
- System design interview preparation
- ERP / SaaS backend reference architecture
- Async Python & FastAPI best practices

---

## 🧑‍💻 Author

Built as a **learning + reference project** to understand how **real-world backend systems are designed**, not just how APIs are written.
