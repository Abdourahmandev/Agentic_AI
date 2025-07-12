# AdventureWorks2022 Database Overview

*Generated from AdventureWorks2022_context.json*

## Introduction
AdventureWorks2022 is a comprehensive sample database designed for demonstrating business processes, analytics, and data science on a realistic dataset. This document provides a data analyst–friendly overview of the database structure, including schemas, tables, columns, data types, views, and other key metadata.

---

## Database Summary
- **Database Name:** AdventureWorks2022
- **Extraction Timestamp:** 2025-07-11 23:15:11
- **Total Schemas:** 18
- **Total Tables:** 71
- **Total Views:** 20
- **Total Stored Procedures:** 8
- **Total Functions:** 11
- **Total Triggers:** 0

---

## Schemas
AdventureWorks2022 is organized into multiple schemas, each grouping related tables and objects. Key business schemas include:
- **HumanResources**: Employee, department, and HR data
- **Person**: Contact and address information
- **Production**: Product, inventory, and manufacturing
- **Purchasing**: Vendors and purchasing data
- **Sales**: Customers, orders, and sales data

Other schemas (e.g., `dbo`, `INFORMATION_SCHEMA`, `sys`, and various `db_*` roles) serve system, metadata, or administrative purposes.

---

## Example Table Structure (HumanResources.Employee)
```
| Column Name         | Data Type      | Nullable | Description (if available) |
|---------------------|---------------|----------|----------------------------|
| BusinessEntityID    | int           | NO       | Employee unique ID         |
| NationalIDNumber    | nvarchar(15)  | NO       | National ID                |
| LoginID             | nvarchar(256) | NO       | Login credentials          |
| OrganizationNode    | hierarchyid   | YES      | Org structure node         |
| OrganizationLevel   | smallint      | YES      | Org hierarchy level        |
| JobTitle            | nvarchar(50)  | NO       | Job title                  |
| BirthDate           | date          | NO       | Date of birth              |
| MaritalStatus       | nchar(1)      | NO       | Marital status             |
| Gender              | nchar(1)      | NO       | Gender                     |
| HireDate            | date          | NO       | Hire date                  |
| SalariedFlag        | bit           | NO       | Salaried employee?         |
| VacationHours       | smallint      | NO       | Vacation hours             |
| SickLeaveHours      | smallint      | NO       | Sick leave hours           |
| CurrentFlag         | bit           | NO       | Currently employed?        |
| rowguid             | uniqueidentifier | NO    | Row unique ID              |
| ModifiedDate        | datetime      | NO       | Last update                |
```

- **Primary Key:** BusinessEntityID
- **Indexes:** (see JSON for details)
- **Foreign Keys:** (see JSON for details)

---

## Views
Views are virtual tables representing complex queries. Example:
- **Purchasing.vVendorWithAddresses**: Combines vendor and address info for reporting.
- **Purchasing.vVendorWithContacts**: Combines vendor and contact info.

---

## How to Use This Metadata
- **Data Exploration:** Use the schema/table/column info to write queries, join tables, and understand relationships.
- **Analytics:** Identify key business tables (e.g., Sales.SalesOrderHeader, Production.Product) for reporting and analysis.
- **ETL/Data Engineering:** Use column types and constraints for data pipelines and validation.
- **Documentation:** This markdown and the JSON file serve as a living data dictionary for your team.

---

## Full Schema & Table List
Below is a summary of all business schemas and their tables. For each table, see the JSON file for full column details, keys, and indexes.

### HumanResources
- Department
- Employee
- EmployeeDepartmentHistory
- EmployeePayHistory
- JobCandidate
- Shift

### Person
- Address
- AddressType
- BusinessEntity
- BusinessEntityAddress
- BusinessEntityContact
- ContactType
- CountryRegion
- EmailAddress
- Password
- Person
- PersonPhone
- PhoneNumberType
- StateProvince

### Production
- BillOfMaterials
- Culture
- Document
- Illustration
- Location
- Product
- ProductCategory
- ProductCostHistory
- ProductDescription
- ProductDocument
- ProductInventory
- ProductListPriceHistory
- ProductModel
- ProductModelIllustration
- ProductModelProductDescriptionCulture
- ProductPhoto
- ProductProductPhoto
- ProductReview
- ProductSubcategory
- ScrapReason
- TransactionHistory
- TransactionHistoryArchive
- UnitMeasure
- WorkOrder
- WorkOrderRouting

### Purchasing
- ProductVendor
- PurchaseOrderDetail
- PurchaseOrderHeader
- ShipMethod
- Vendor

### Sales
- CountryRegionCurrency
- CreditCard
- Currency
- CurrencyRate
- Customer
- PersonCreditCard
- SalesOrderDetail
- SalesOrderHeader
- SalesOrderHeaderSalesReason
- SalesPerson
- SalesPersonQuotaHistory
- SalesReason
- SalesTaxRate
- SalesTerritory
- SalesTerritoryHistory
- ShoppingCartItem
- SpecialOffer
- SpecialOfferProduct
- Store

---

## Additional Notes
- **System Schemas:** `dbo`, `sys`, `INFORMATION_SCHEMA`, and `db_*` are mostly for system or admin use.
- **Constraints & Indexes:** See the JSON for detailed info on keys, constraints, and indexes for each table.
- **Stored Procedures & Functions:** Business logic is implemented in stored procedures and functions, also detailed in the JSON.

---

## For Data Analysts
- Use this document and the JSON as your go-to reference for understanding the AdventureWorks2022 database.
- For deeper analysis, always check the JSON for up-to-date metadata, especially when building new queries or data models.
- If you need a specific table or relationship explained, refer to the relevant section in the JSON or ask for a focused summary. 