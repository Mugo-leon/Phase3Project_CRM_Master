# CRM Master

## Problem Statement

Managing leads and sales representatives efficiently is crucial for a company's success. Without a proper system, leads may be forgotten, and sales representatives might face challenges in identifying their assigned prospects. This can lead to confusion and unhealthy competition among sales associates. Companies also need to recognize referrers so that they know who to reward to ensure steady supply of leads.

## Solution

CRM Master is a Command-Line Interface (CLI) tool designed to address these challenges. It enables sales representatives and managers to track leads, associate them with specific sales representatives, and reward converted customers who refer leads. The CLI will also allow managers to replace sales associates in the database in case the previous ones leave the company. The CLI will also allow managers to delete leads not worthy of further pursuit on the recommendation of the sales associates. 

## Key Features

- Managers can track leads assigned to sales representatives.
- Managers can identify referrals from converted customers.
- A reward system is implemented for converted customers who refer 3 or more leads.

## Minimum Viable Product (MVP)

- Managers can view leads assigned to each sales representative.
- Managers can identify referrals from converted customers.
- Managers can see which converted customers are eligible for a 20% discount.
- Managers can add a new sales associate
- Managers can add a lead and the converted customer who referred the lead
- Managers can change names of sales associates
- Managers can delete leads that sales associates feel are lost leads

## Project Structure

The project is structured with the following components:

- **lib/seeds.py:** Contains seed data and functions to initialize the database.
- **lib/models/models.py:** Defines the SQLAlchemy ORM models for Sales Associate, Leads, and Converted Customers.
- **lib/cli.py:** Implements the CLI functionality, including listing leads, referring customers, discount eligibility, and lead reassignment.
- **lib/main.py:** Entry point for the CLI commands.

## Setup

1. Install dependencies: `pipenv install`
2. Run seed data script: `pipenv run python lib/seeds.py`
3. Execute the CLI: `pipenv run python lib/main.py`

## Dependencies

- SQLAlchemy
- Click

