#### Data Population

The CMDB allows for accurate data acquisition through:

- Agent-less auto-discovery of known and unknown CIs
- Existing integrations to third party data sources
- Additional integrations using web services or other methods

Built-in data reconciliation and normalization features ensure consistently accurate and useful data.

![[Pasted image 20241013095332.png]]

**ServiceNow Discovery** can be implemented to easily and accurately populate and maintain the CMDB with CI data that is constantly being rediscovered and refreshed in the CMDB. Fully integrated and agent-less, ServiceNow Discovery automatically identifies the type of CI it is interacting with and then launches additional probes, sensors, and patterns that are appropriate to that device to gather further information and attributes.

**ServiceNow Service Mapping** overlays service maps onto existing configuration data to connect CIs underlying a given service, making the CMDB service aware.

The CMDB also integrates with the most common infrastructure platforms such as VMware vCenter, Microsoft System Center Configuration Manager, and Google Cloud Platform as well as endpoint management products.

Additionally, data may be imported into the CMDB through **IntegrationHub ETL** (a ServiceNow Store application), **import sets, web services, direct database imports, and Excel files.** Transform maps, the Identification and Reconciliation Engine, and business rules enable inbound data to be mapped to target tables and fields, transformed, merged, and coalesced.

The CMDB leverages the NOW Platform features such as the **Identification and Reconciliation Engine (IRE)** and field normalization to automatically check uniqueness of a CI. Reconciliation Rules allow only authorized data sources to update specific CI classes, normalizes the data, and then loads the data into the CMDB to ensure the most recent and accurate profile of that CI.

##### **Service Aware CMDB**

ServiceNow's Service Mapping technology discovers and provides a clear, graphical view of complex IT infrastructure and service relationships. IT professionals can click through the service map, filtering data, focusing in on specific CIs, and viewing impact and risk alongside in-flight operational activities such as incident, problem, and change requests.

Administrators, system owners, and service owners can quickly identify configuration drift, unplanned changes, and incident history to understand the health of CIs they are responsible for and the operational activities directly or indirectly impacting those CIs.

#### **Common Services Data Model Overview**

The Common Services Data Model (CSDM) represents a standard and shared set of service related definitions across the ServiceNow products and platform. The CSDM enables and supports true service level reporting, while providing prescriptive guidance on service modeling within the CMDB. These service-related definitions span the ServiceNow product portfolio and the Now Platform.

The data model is a CMDB framework across our products and platform that will enable and support multiple configuration strategies. The CSDM includes best practices related to the proper modeling of data using base system tables and relationships. Many ServiceNow products have a dependency on data within this data model.

- **Common Service**: A standard and shared set of service related definitions across our products and platform that will enable and support true service level reporting.
    
- **Data Model**: A CMDB Framework across our products and platform that will enable and support multiple configuration strategies.

**CMDB Stakeholders**

When starting out on a CMDB journey, there are potentially many stakeholders that can realize value from a robust and accurate CMDB. Each stakeholder will have different goals and outcomes they want to realize from a CMDB implementation.  

Agreement upon configuration management goals and objectives is essential to ensure stakeholders are in alignment and agree upon the priorities established. Your configuration management efforts should be clearly and explicitly tied to the strategic goals of your organization and to the tactical goals of your IT department.

CMDB enables you to create a service dependency map so that you can relate events, incidents, problems, and requests for change to service impact. **To determine the specific CI information** required to support these capabilities and build organizational buy-in, **you will need to involve the right stakeholders**. This stakeholder group should include the process owners, process managers, and other subject matter experts for each of the processes.

