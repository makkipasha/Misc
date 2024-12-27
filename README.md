This ticket will focus on planning the segregation of alerts by severity to improve incident response and minimize alert fatigue. The planning activities will include:

Analysis of Current Alerts: Review existing alerts to categorize them into the new severity levels: Critical (Sev 0), High-Priority (Sev 1), and Informational (Sev 2).
Stakeholder Engagement: Conduct meetings with key stakeholders from IT operations and business units to define the criteria for each alert category and understand the impact.
Implementation Strategy: Develop a strategy for implementing the new alert categories, including the technical requirements and changes needed in our current monitoring tools.
Testing Plan: Outline a testing plan to validate the effectiveness of the new alert categories before full-scale deployment.
This planning will ensure that our alert system is effectively organized to address incidents with appropriate urgency and precision.

Jira Ticket 2: Documenting the Segregation and Classification of Alerts Process
Title: Documentation of the New Alert Segregation and Classification System

Description: Develop comprehensive documentation for the new system of alert segregation based on severity. This documentation will serve as a foundational guide for configuring and maintaining the alert system and will include:

Documentation of Alert Categories: Detailed descriptions of each alert category (Sev 0, Sev 1, Sev 2), including examples and the actions required for each.
Configuration Instructions: Step-by-step instructions on how to configure the new alert categories within our existing alert management tools.
Operational Guidelines: Best practices for monitoring and responding to alerts of different severities to ensure effective incident management.
Review and Update Procedures: Guidelines on how to periodically review and update the alert categories to adapt to changing business needs and technological advancements.
This documentation will be essential for ensuring that all team members are aligned on the new alert system, facilitating consistent and effective responses to system alerts.


Action Plan :


1: Preparation
  1. Get the Pace Certificate Request Form Filled
    - Owner: Assigned team member
    - Steps:
      1. Identify all certificates that need the Pace Certificate Request form.
      2. Contact the relevant stakeholders or certificate owners.
      3. Share the form and guide the stakeholders in filling it out correctly.
      4. Follow up to ensure timely submission.
      5. Verify the completeness and accuracy of the submitted forms.
    - Deliverable: Completed and verified Pace Certificate using Request Forms and getting installed on workstation.

  2. Gather Inventory of All Certificates**
    - Owner: Security or Infrastructure team
    - Steps:
      1. Create a list of all certificates in use, including:
         - Certificate name
         - Issuing authority
         - Expiry date
         - Environment (Dev, QA, Prod)
      2. Identify certificates that are expired or nearing expiry.
      3. Document the renewal process for each certificate.


2: Immediate Renewal Tasks
  3. Renew All Expired Certificates
    - Owner: Assigned team member(s)
    - Steps:
      1. Prioritize renewing certificates that are already expired or critical to production environments.
      2. Follow the documented renewal process for each certificate.
      3. Test the renewed certificates in the appropriate environments (Dev/QA/Prod).
      4. Update the inventory list with new expiry dates.
    - Deliverable: Renewed and functional certificates across all environments.


3: Proactive Monitoring
  4. Create Alerts for Upcoming Expiry of Certificates
    - Owner: Monitoring/Automation team
    - Steps:
      1. Integrate certificate tracking with monitoring tools (e.g., Zabbix, Datadog, or custom scripts).
      2. Set up alerts to trigger notifications at least 30 days before expiry.
      3. Configure escalation notifications to stakeholders and decision-makers.
      4. Test alert functionality to ensure accurate and timely notifications.
    - Deliverable: Fully functional alert system for certificate expiry.



4: Automation
  5. Automate Renewal of Certificates
    - Owner: DevOps/Automation team
    - Steps:
      1. For NiFi Certificates:
         - Document the renewal and deployment process for NiFi certificates.
         - Create an automated script or pipeline (e.g., using Jenkins, GitLab CI/CD).
         - Integrate tools like Certbot for Let's Encrypt certificates or APIs for enterprise CAs.
      2. Deploy Automation in the Development Environment:
         - Validate the automation process in the development environment.
         - Ensure successful certificate deployment to the NiFi application.
      3. Extend Automation to Higher Environments:
         - After successful testing in Dev, extend to QA, and finally to Production.
      4. Generalize Automation for Other Certificates:
         - Identify patterns for automating renewal and deployment of other certificates.
         - Develop reusable templates for automation scripts.
      5. Document and Train:
         - Document the entire automation process.
         - Train team members on the use and maintenance of the automated system.
    - Deliverable: Automated certificate renewal and deployment process operational across all environments.


5: Continuous Improvement
  6. Regular Reviews and Updates
    - Owner: Security and Infrastructure teams
    - Steps:
      1. Review the alert system to ensure it is capturing all certificates.
      2. Evaluate the performance of the automation system and make necessary improvements.
      3. Update the certificate inventory regularly to reflect changes.
      4. Stay informed on industry best practices for certificate management.
