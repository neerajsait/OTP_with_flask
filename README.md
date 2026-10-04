# OTP_with_flask

> A Flask signup flow that emails and verifies a one-time code.

## Overview

The app generates a six-digit OTP, sends it through Flask-Mail, and checks the submitted code in a simple browser workflow. The current implementation keeps codes in process memory.

## What’s in this repo

- Signup form and OTP request route
- Email delivery through SMTP
- Code verification and a follow-up page

## Stack

Python, Flask, Flask-Mail, SMTP, HTML templates.

## Getting started

1. Install Flask and Flask-Mail, then configure a test SMTP account locally without committing live credentials.
2. Run `python app.py` and open the local address; test only with an account you control.

## Notes

The checked source uses placeholder credentials and in-memory OTP storage. Do not use this implementation for real accounts; add expiry, rate limits, secure secret handling, and persistent/session-safe storage first.
