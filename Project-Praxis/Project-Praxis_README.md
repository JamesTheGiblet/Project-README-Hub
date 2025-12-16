## **Project: Praxis**
A Modular, Self-Improving AI Assistant



#### **The Motivation: Why Build This?**

I wanted to build a real J.A.R.V.I.S.-like AI assistant. Most "build your own J.A.R.V.I.S." tutorials online are just glorified `if/else` scripts or thin wrappers around a single API. They're not smart, they can't learn, and they can't grow.

Praxis is my ground-up attempt to build it the right way. It's an AI assistant designed from day one with a long-term vision: to create a system that is modular, genuinely intelligent, and eventually, capable of contributing to its own development.

---
#### **The Design Philosophy**

The project is guided by a few core principles:
* **Goal: Self-Improvement:** The ultimate goal is for the system to become autonomous enough to monitor its own performance, identify its own flaws, and suggest or even implement improvements.
* **Modular by Design:** The architecture is built on "skills"—small, self-contained Python modules that can be loaded, updated, or removed on the fly. This makes the system incredibly flexible and easy to extend.
* **Emergent Behavior:** The idea is that complex, intelligent behaviors will arise from the interaction of many simple, well-defined skills, rather than being hard-coded from the top down.
* **Context is Key:** The AI should always be aware of the ongoing conversation, the user it's talking to, and its own capabilities.
* **Iterative Growth:** Like any good piece of software, this system evolves. Changes are built upon the previous version, not thrown out and replaced.

---
#### **What It Can Do Now (Current Capabilities)**

Praxis is already a powerful and capable assistant.
* **It's Built on Skills:** The entire system is modular. New capabilities are added simply by dropping a new Python file into the `skills/` directory. The AI automatically knows about any new skills and how to use them without needing manual updates.
* **The Brain is the Gemini API:** It uses Google's Gemini API for its core natural language understanding. It can interpret complex commands, hold a contextual conversation, and reason through multi-step tasks.
* **It Has a Memory (A SQLite Database):** Praxis uses a local SQLite database to track everything: which skills are used most often, what errors have occurred, user feedback, and user-specific information. This data is the foundation for all learning and self-improvement.
* **It Gets to Know You:** It has skills for managing a user profile, allowing it to store preferences and facts about you to personalize the interaction. It can even proactively start a conversation based on your interests if it's been idle for a while.
* **It Can Manage Itself (Basics):** It has skills to analyze its own performance (e.g., "what are your most-used skills?") and even a foundational `skill_refinement_agent` that can use the LLM to try and fix skills that are throwing errors.

---
#### **Recent Upgrades**

I've recently pushed several updates focused on improving the core intelligence (CIQ) and conversational ability (CEQ).
* **Smarter Coding (Test & Repair Loop):** When Praxis generates code that fails a unit test, it now automatically feeds the error, the original request, and the bad code back to the LLM to get a corrected version. This has dramatically improved its coding accuracy.
* **Better Context (RAG Foundation):** The system can now retrieve relevant snippets from its own source code or API docs and include them in prompts to the LLM. This gives the AI better context for generating more accurate, domain-specific code.
* **Smarter Conversation (It Adapts to Your Mood):** It now performs sentiment analysis on user input. If it detects frustration, it can adjust its system prompt to be more patient and supportive in its response.
* **More Transparent Thinking (Structured JSON Output):** The LLM's responses for command processing are now structured in JSON. This includes not just the answer, but also metadata like an `explanation` of its reasoning and a `confidence_score`, making the AI's internal state easier to work with.

---
#### **Current Focus: The Feedback Loop (Phase 3)**

The top priority right now is building robust systems for continuous improvement.
* **Automated Testing:** Integrating the CIQ/CEQ benchmark tests into a CI/CD pipeline so every code change is automatically evaluated for performance regressions.
* **User Feedback:** The UI now has simple 👍/👎 buttons so I can give immediate feedback on responses. This data is logged and linked to the specific interaction.
* **Curating Training Data:** Every successful interaction (e.g., a thumbs-up response, or generated code that passes all tests) is flagged. This creates a high-quality dataset of "gold standard" examples that will be invaluable for future fine-tuning of the core model.

---
#### **The Roadmap**

**Perfect is the imaginary friend of never shipped.** This is a long-term project with a clear, phased plan.
* **Phase 4: Guided Self-Improvement:** The current focus. This involves making the skill refinement agent more robust, allowing Praxis to suggest improvements to its own prompts, and deepening its user profiling capabilities.
* **Phase 5: Adaptive Interfaces & Embodiment:** Building out GUIs and APIs, and potentially integrating Praxis into physical or simulated environments to test its adaptability.
* **Phase 6: Advanced Cognitive Development:** This is the big one. Implementing more sophisticated long-term memory, creativity, and open-ended goal-setting.

This is the long game. Building a truly intelligent system is a marathon, not a sprint. **The code is the proof**, and every new feature is another step on that road.
