azure__pricing__calculator = AzurePricingCalculator()

azure__pricing__calculator.add__service("Azure Data Factory", activities_per_month=200)

azure__pricing__calculator.add__service("Azure Data Lake Storage Gen2", storage_size_gb=1020, access_tier="Hot")


azure__pricing__calculator.add__service("Azure Synapse Analytics", data_size_gb=1020, performance_tier="DW300c")

azure__pricing__calculator.add__service("Azure Logic Apps", runs_per_month=20)


azure__pricing__calculator.add__service("Azure Blob Storage", storage_size_gb=60, access_tier="Hot")


azure__pricing__calculator.add__service("Azure Virtual Network")
azure__pricing__calculator.add__service("Azure VPN Gateway", gateway_type="Standard")


azure__pricing__calculator.add__service("Azure ExpressRoute", bandwidth_mbps=1000)


azure__pricing__calculator.add__service("Azure Monitor", resources_to_monitor=["ADF", "ADLS", "Synapse", "LogicApps", "BlobStorage", "VirtualNetwork", "VPNGateway", "ExpressRoute"])

estimate__link = azure__pricing__calculator.generate__link()
print("Azure Pricing Calculator Estimate Link: ", estimate__link)
