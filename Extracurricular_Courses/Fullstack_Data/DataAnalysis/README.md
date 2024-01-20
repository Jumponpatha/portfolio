# Mini Project - Data Analysis

## Topic: Food Retail Analysis

### Association Rule Mining
Market Basket Analysis is one of the key techniques used by large retailers to uncover associations between items. It works by looking for combinations of items that occur together frequently in transactions. To put it another way, it allows retailers to identify relationships between the items that people buy.

Association Rules are widely used to analyze retail basket or transaction data and are intended to identify strong rules discovered in transaction data using measures of interestingness, based on the concept of strong rules.

### Details of the dataset
The dataset has 5,197,681 rows of the purchase orders of people from the food retail stores. These orders can be analysed and association rules can be generated using Market Basket Analysis by algorithms like Apriori Algorithm.

### Apriori Algorithm
Apriori is an algorithm for frequent itemset mining and association rule learning over relational databases. It proceeds by identifying the frequent individual items in the database and extending them to larger and larger item sets as long as those item sets appear sufficiently often in the database. The frequent itemsets determined by Apriori can be used to determine association rules which highlight general trends in the database: this has applications in domains such as market basket analysis.

### About Dataset
1. **transactions** : household level data over a period of two years from four categories: Pasta, Pasta Sauce, Syrup, and Pancake Mix.
    - upc	- Standard 10 digit UPC.
    - dollar_sales - Amount of dollars spent by the consumer
    - units	- Number of products purchased by the consumer
    - time_of_transaction -	The time of transaction(military time)
    - geography	- Distinguishes between two large geographical regions, possibly values are 1 or 2
    - week -	Week of the transaction, values are from 1 to 104
    - household	- Unique households
    - store	- Unique stores
    - basket	- Unique baskets/trips to store
    - day	- day of the transaction, possible values are from 1 to 728
    - coupon -	Indicates coupon usage, 1 if used, 0 otherwise

2. **product lookup** : detailed product information
    - upc	- Standard 10 digit UPC.
    - product_description -	Description of product
    - commodity	- specifies the four product categories under consideration
    - brand	- Specific brand of item
    - product_size	- Specifies package size of product

3. **causal lookup** : trade activity for each product/week
    - upc -	Standard 10 digit UPC.
    - store	- Identifies unique store
    - week	- Week of transaction, possible values are 1 through 104
    - feature_desc -	Describes product location on weekly mailer
    - display_desc	- Describes temporary in-store display
    - geography	- Distinguishes between two large geographical regions, possible values are 1 or 2

4. **store lookup** : store and it’s zip code
    - store	Identifies - unique stores
    - store_zip_code -	5 digit zip code
