
**Configuration Item (CI)** - Physical and logical components of an infrastructure that needs to be managed to deliver a product or service and are currently, or soon will be, under configuration management.  For example, a network device, a server, an application, a delivery truck, or service.

**Attributes** - Information that further describes a CI such as a name, serial number, manufacturer, operating system.

**Relationship Type** - Include the relationships between configuration items. For example, a web application might read data from a specific database, which in turn might depend on a piece of underlying hardware.

**Class** - Describes a table that contains and represents a specific type or group of CIs that share common attributes  such as a Windows Server, Linux Server, Printer, Virtual Machine, Vehicle, Animal etc.

**Configuration Management System (CMS)** - A set of tools and databases that are used to manage an organizations configuration data.

**Configuration Management Database (CMDB)** - A database used to store configuration records throughout their Lifecycle. The Configuration Management System maintains one or more CMDBs, and each CMDB stores attributes of CIs, and Relationships with other CIs.

**Base Table** - The core Configuration Item [cmdb_ci] table, which stores the basic attributes of all the CIs. All configuration item classes extend from this table including all hardware and applications.

**CI Reclassification** - Is a CI whose class has been upgraded, downgraded, or switched. An example of an upgraded CI is a Server record that was upgraded from the Server [cmdb_ci_server] class to the Windows Server [cmdb_ci_win_server] class.

**CI Class Upgrade** - The CI class is updated to a class that is less generic in the class hierarchy, and the newly assigned class has additional attributes. For example, an upgrade occurs if a CI is moved from the Server [cmdb_ci_server] class to the Windows Server [cmdb_ci_win_server] class.

**CI Class Downgrade** - The CI class is updated to a class that is more generic in the class hierarchy, and the newly assigned class has less attributes. For example, a downgrade occurs if a CI is moved from the Windows Server [cmdb_ci_win_server] class to  the Server [cmdb_ci_server] class.

**CI Class Switch** - The CI class is in a different branch in the class hierarchy and has a different set of attributes than the current class. For example, reclassifying a CI from the Linux Server [cmdb_ci_linux_server] class to the Windows Server [cmdb_ci_win_server] class.

**Parent and Child Class** - A table that extends another table is called a child class, and the table it extends is the parent class. A table can be both a parent and child class both extending and providing extensions for other tables. For example, the Server table extends the Computer table and the Windows Server table extends the Server table, thus making the Server table both a Parent and Child class.

**Asset vs. CI** - On the Now platform, when creating a hardware asset, a corresponding CI will be automatically created or when a CI is discovered for the first time and inserted into the CMDB, a corresponding asset record will be automatically created. The asset and the CI is connected through out the CI/Asset lifecycle.

**Asset:**

- Often starts  during the procurement process, but may be created when a discovery tool finds the CI for the first time
- Is part of the financial lifecycle

**Configuration Item (CI):**

- Often starts when a discovery tool finds the CI for the first time, but may be created during the procurement process
- Is part of the technical operations

**Asset DB vs. CMDB** - 
- Asset DB is inventory + financial data
- CMDB is inventory + relationships

**CMDB vs. Authoritative Sources** - 
The CMDB is the authoritative source of some information:

- Support group
- Contact
- Owner

The CMDB is not the authoritative source of all information:

- Contents of all server and application configuration files
- Server log file

**Common Services Data Model (CSDM)** - Represents a standard and shared set of service related definitions across ServiceNow products and the NOW platform that enables and supports true service level reporting while providing prescriptive guidance on service modeling within the CMDB. These service-related definitions span the ServiceNow® product portfolio and the Now Platform®.

**Application Service** - A set of interconnected applications and hosts which are configured to offer a service to the organization. Application services can be internal, like an organization email system or customer-facing, like an organization website.

**Application** - Applications that comprise an application service as configuration items (CIs). The various Applications and the relationships between them, that comprise an application service, are stored in the CMDB. (i.e. Tomcat, Apache, Microsoft SQL, Oracle, IIS).

**DevOps** - Consists of developers who build applications and the operations groups who deploy and maintain them within an enterprise. In a DevOps environment, these two groups are combined into one in order to work more effectively together to accelerate and improve service delivery.