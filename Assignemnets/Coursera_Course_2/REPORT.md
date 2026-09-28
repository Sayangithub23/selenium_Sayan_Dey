# Selenium Practice Scripts Report

## Scope

Reviewed all 14 files present in the workspace: Python scripts demonstrating Selenium browser automation. The examples mainly use public practice websites and Firefox or Chrome. This report describes the code as written; the scripts were not executed.

## Overview

The workspace is a collection of learning exercises rather than a packaged application. It covers opening browser tabs, interacting with YouTube, handling JavaScript alerts, drag-and-drop, keyboard input, copying and pasting, mouse hover menus, scrolling, and a form submission with checks. There is no shared configuration, dependency manifest, test suite, or common runner.

## File inventory

| File | Purpose |
|---|---|
| `1st.py` | Opens Google in Firefox, creates a new tab, then opens YouTube. |
| `2nd.py` | Opens YouTube in two tabs, searches for “Numb”, opens the first result, attempts to play it, then closes the tab and browser. |
| `alert_pop_up.py` | Clicks the “Confirmation Alert” button, prints the alert text, and accepts it. |
| `alert_practice.py` | Uses an explicit wait to handle a “Simple Alert”. |
| `drag_drop.py` | Locates a drag source and drop target by text/ID, scrolls them into view, and performs a manual drag action. |
| `drag-and-drop.py` | Performs drag-and-drop using element IDs and Selenium’s `drag_and_drop`. |
| `keyboard_actions.py` | Enters text into a textarea, selects and replaces it with keyboard actions, then presses Enter. |
| `keys-assignment.py` | Uses Chrome to copy text from one textarea and paste it into another on text-compare.com. |
| `mini_automation.py` | Fills and submits Selenium’s sample web form, verifies the title and confirmation, and saves a screenshot. Includes exception handling and guaranteed browser cleanup. |
| `mouse_hover.py` | Scrolls to “Point Me”, hovers, and clicks the “Mobiles” submenu. |
| `mouse.py` | A more instrumented version of the hover exercise, with status output and `finally` cleanup. |
| `pop_up_with_ok.py` | Clicks the confirmation button by ID, waits for an alert, prints its text, and accepts it. |
| `scroll.py` | Uses Chrome to scroll to and click the About link on text-compare.com. |
| `test.py` | Uses Firefox and ActionChains to enter, select, copy, and paste text between practice-page fields. |

## Findings

### Strengths

- The exercises show a useful range of Selenium APIs: `By` locators, `ActionChains`, keyboard keys, alerts, browser windows, JavaScript scrolling, and explicit waits.
- `mini_automation.py` is the most complete example: it checks expected page state, validates the submitted result, captures a screenshot, handles common failures, and closes the browser in `finally`.
- The alert, drag-and-drop, and hover examples include explicit waits in several places, which is more reliable than relying entirely on fixed delays.

### Reliability and maintainability opportunities

- Many scripts create a browser without `try/finally`; if an interaction fails, the browser may remain open. `mouse.py` and `mini_automation.py` demonstrate safer cleanup patterns.
- Fixed `time.sleep()` calls appear in `2nd.py`, `alert_pop_up.py`, `drag_drop.py`, and `mouse_hover.py`. Condition-based waits would usually reduce flakiness and unnecessary delay.
- `keys-assignment.py` and `scroll.py` use Chrome, while the remaining browser exercises mostly use Firefox. Running all scripts therefore requires both browsers (or changing the examples consistently).
- Copy/paste exercises depend on clipboard behavior and browser/OS keyboard handling, so they may behave differently across environments.
- YouTube controls, practice-site markup, and text-compare.com selectors can change. Some interactions may also be affected by consent dialogs, ads, login state, or browser policies.
- `2nd.py` uses sleeps for YouTube loading and assumes the first video result and a button labeled “Play” are available. Those assumptions can fail as the page changes.
- `mini_automation.py` catches broad `Exception` and prints the error without re-raising it. This is friendly for a demo, but a caller or automated runner could interpret a failed run as successful unless an exit status is added.
- Similar exercises are duplicated (`mouse.py`/`mouse_hover.py`, `drag_drop.py`/`drag-and-drop.py`, and the two alert examples). Consolidating common setup and waits would reduce repetition if this grows beyond practice scripts.

## Running the scripts

The scripts require Python with Selenium installed and a compatible browser. Selenium Manager is mentioned in `mini_automation.py` for Firefox driver management; the Chrome examples also need Chrome available. Several scripts rely on network access to third-party sites. There is no `requirements.txt` or project-level setup documentation in the reviewed workspace.

## Suggested next steps

1. Add a dependency/setup file and a short README describing browser requirements and how to run each exercise.
2. Use explicit waits for page conditions instead of fixed sleeps where possible.
3. Apply `try/finally` browser cleanup consistently.
4. Add assertions for outcomes in exercises that currently only print a completion message.
5. Keep browser choice and locator conventions consistent, or document why an exercise uses a different browser.
