# Discussion: AI Hardware & Cloud Strategy

**Jeff Johnson | Eighth Class | Module 2 Discussion**

---

## Part 1 — Hardware Deep Dive: Google TPU v4

Think of a regular CPU like a single really smart employee who can do any job in the office, but can only handle one task at a time. Google's TPU v4 is physically built differently — it contains a structure called a systolic array, which is a giant grid of 16,000 tiny multiplier units all hardwired together, so instead of doing one math operation at a time, every unit fires simultaneously and passes its result to the next unit in the grid, like an assembly line where every station works at once. A gaming GPU is somewhere in between, but it still wastes a chunk of its chip on drawing game graphics — shadows, lighting, textures — hardware that sits completely idle during AI training. Because the TPU dedicates every part of its physical design to matrix math and nothing else, it can crunch through about 275 trillion calculations per second, versus roughly 8 trillion for a top-of-the-line regular processor.

---

## Part 2 — Strategic Analysis: Anthropic's Multi-Cloud Strategy

Anthropic put its Claude AI on all three major cloud platforms — Amazon, Google, and Microsoft — instead of picking just one. The first reason is practical: if one cloud crashes or runs out of server space, Claude keeps working by switching to one of the other two, and no customer notices anything. The second reason is about money and relationships — both Amazon and Google have each invested billions of dollars into Anthropic, so choosing one cloud over the other would anger a major backer, and saying yes to all three keeps everyone happy. The third reason is about customers — imagine a hospital that is only allowed to store its data on Google's servers for legal reasons; if Claude were only on Amazon, that hospital could never use it, so by being everywhere, Anthropic makes sure no customer is left out just because of which cloud they're stuck on. Finally, being on all three gives Anthropic power in negotiations — if Amazon tries to charge more or change the deal, Anthropic can threaten to lean into Google or Microsoft instead, which is leverage they would completely lose if they had gone exclusive with anyone.


