- [Intro](#intro)

## Intro

- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv

Say you have an array for which the i-th element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.
Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.





## Topics

- `Dynamic Programming`


## DP

- 给定一个数组, 用来表示一天内价格变化. 最多交易k次, 求最大收益 https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/ dp/hard


```csharp
int stockTrading(){
    // 这种情况千万不要用两层循环.
    int maxProfit=0,buy=INT_MAX;
    for(int i=0;i<prices.size();i++){
        buy = min(buy, prices[i]); // 每步确保买入价最小
        maxProfit = max(prices[i]-buy, maxProfit); // 从而得到最大的利润
    }
    return maxProfit;
}
int StockTrading_(vector<int>& prices) {
    int maxProfit=0,buy=INT_MAX;
    for(int i=0;i<prices.size();i++){
        buy = min(buy, prices[i]);
        maxProfit = max(prices[i]-buy, maxProfit);
    }
    return maxProfit;
}
int StockTrading_II(vector<int> &prices) {
    int max=0, begin=0, end=0;
    bool up=false, down=false;
    for (int i=1; i<prices.size(); i++) {
        if (prices[i] > prices[i-1] && up==false){ // goes up
            begin = i-1;
            up = true;
            down = false;
        }
        
        if (prices[i] < prices[i-1] && down==false) { // goes down
            end = i-1;
            down = true;
            up = false;
            max += (prices[end] - prices[begin]);
        }
    }
    // edge case 
    if (begin < prices.size() && up==true){
        end = prices.size() - 1;
        max += (prices[end] - prices[begin]);
    }
    
    return max;
}


int StockTrading_III(vector<int> &prices) {
    if (prices.size()<=1) return 0;
    
    int n = prices.size();
    
    vector<int> forward(n);
    forward[0] = 0;
    int lowestBuyInPrice = prices[0];
    for(int i=1; i<n; i++){
        forward[i] = max(forward[i-1], prices[i] - lowestBuyInPrice);
        lowestBuyInPrice = min(lowestBuyInPrice, prices[i]);
    }
    
    vector<int> backward(n);
    backward[n-1] = 0;
    int highestSellOutPrice = prices[n-1];
    for(int i=n-2; i>=0; i--){
        backward[i] = max(backward[i+1], highestSellOutPrice - prices[i]);
        highestSellOutPrice = max(highestSellOutPrice, prices[i]);
    }
    
    int max_profit = 0;
    for(int i=0; i<n; i++){
        max_profit = max(max_profit, forward[i]+backward[i]);
    }
    
    return max_profit;
}



int StockTrading_IV(int k, vector<int> &prices) {
    int ndays = prices.size();
    
    // error case
    if (ndays<=1) return 0;
    
    // Edge case
    // ---------
    // if the number of transactions is too many, it means we can make 
    // as many transactions as we can, that brings us the problem back to 
    // Best-Time-To-Buy-And-Sell-Stock-II which can be simply solve in O(n) 
    // by using a greedy approach.
    if(k > ndays/2){
        int sum = 0;
        for (int i=1; i<ndays; i++) {
            sum += max(prices[i] - prices[i-1], 0);
        }
        return sum;
    }
    
    //DP solution - O(kn) complexity 
    vector< vector<int> > dp (k+1, vector<int>( ndays+1, 0));
    
    for(int i=1; i<=k; i++) {
        int t = dp[i-1][0] - prices[0];
        for (int j=1; j <= ndays; j++) {
            dp[i][j] = max(dp[i][j-1], t + prices[j-1]);
            if ( j < ndays ) {
                t = max(t, dp[i-1][j] - prices[j]);
            }
        }
    }
    
    return dp[k][ndays];
    
}

// Time:  O(n)
// Space: O(1)
int StockTrading_cooldown_1(vector<int>& prices) {
    if (prices.empty()) {
        return 0;
    }
    vector<int> buy(2), sell(2), coolDown(2);
    buy[0] = -prices[0];
    for (int i = 1; i < prices.size(); ++i) {
        // Bought before or buy today.
        buy[i % 2] = max(buy[(i - 1) % 2], coolDown[(i - 1) % 2] - prices[i]);
        // Sell today.
        sell[i % 2] = buy[(i - 1) % 2] + prices[i];
        // Sold before yesterday or sold yesterday.
        coolDown[i % 2] = max(coolDown[(i - 1) % 2], sell[(i - 1) % 2]);
    }
    return max(coolDown[(prices.size() - 1) % 2], sell[(prices.size() - 1) % 2]);
}

// Time:  O(n)
// Space: O(n)
int StockTrading_cooldown_2(vector<int>& prices) {
    if (prices.empty()) {
        return 0;
    }
    vector<int> buy(prices.size()), sell(prices.size()), coolDown(prices.size());
    buy[0] = -prices[0];
    for (int i = 1; i < prices.size(); ++i) {
        // Bought before or buy today.
        buy[i] = max(buy[i - 1], coolDown[i - 1] - prices[i]);
        // Sell today.
        sell[i] = buy[i - 1] + prices[i];
        // Sold before yesterday or sold yesterday.
        coolDown[i] = max(coolDown[i - 1], sell[i - 1]);
    }
    return max(coolDown[prices.size() - 1], sell[prices.size() - 1]);
}

// Time:  O(n)
// Space: O(1)
int StockTrading_fee(vector<int>& prices, int fee) {
    int cash = 0, hold = -prices[0];
    for (int i = 1; i < prices.size(); ++i) {
        cash = max(cash, hold + prices[i] - fee);
        hold = max(hold, cash - prices[i]);
    }
    return cash;
}
```
 



- 给定一个数组, 用来表示一天内价格变化. 最多交易k次, 求最大收益 https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/ dp/hard


```csharp
int stockTrading(){
    // 这种情况千万不要用两层循环.
    int maxProfit=0,buy=INT_MAX;
    for(int i=0;i<prices.size();i++){
        buy = min(buy, prices[i]); // 每步确保买入价最小
        maxProfit = max(prices[i]-buy, maxProfit); // 从而得到最大的利润
    }
    return maxProfit;
}
int StockTrading_(vector<int>& prices) {
    int maxProfit=0,buy=INT_MAX;
    for(int i=0;i<prices.size();i++){
        buy = min(buy, prices[i]);
        maxProfit = max(prices[i]-buy, maxProfit);
    }
    return maxProfit;
}
int StockTrading_II(vector<int> &prices) {
    int max=0, begin=0, end=0;
    bool up=false, down=false;
    for (int i=1; i<prices.size(); i++) {
        if (prices[i] > prices[i-1] && up==false){ // goes up
            begin = i-1;
            up = true;
            down = false;
        }
        
        if (prices[i] < prices[i-1] && down==false) { // goes down
            end = i-1;
            down = true;
            up = false;
            max += (prices[end] - prices[begin]);
        }
    }
    // edge case 
    if (begin < prices.size() && up==true){
        end = prices.size() - 1;
        max += (prices[end] - prices[begin]);
    }
    
    return max;
}


int StockTrading_III(vector<int> &prices) {
    if (prices.size()<=1) return 0;
    
    int n = prices.size();
    
    vector<int> forward(n);
    forward[0] = 0;
    int lowestBuyInPrice = prices[0];
    for(int i=1; i<n; i++){
        forward[i] = max(forward[i-1], prices[i] - lowestBuyInPrice);
        lowestBuyInPrice = min(lowestBuyInPrice, prices[i]);
    }
    
    vector<int> backward(n);
    backward[n-1] = 0;
    int highestSellOutPrice = prices[n-1];
    for(int i=n-2; i>=0; i--){
        backward[i] = max(backward[i+1], highestSellOutPrice - prices[i]);
        highestSellOutPrice = max(highestSellOutPrice, prices[i]);
    }
    
    int max_profit = 0;
    for(int i=0; i<n; i++){
        max_profit = max(max_profit, forward[i]+backward[i]);
    }
    
    return max_profit;
}



int StockTrading_IV(int k, vector<int> &prices) {
    int ndays = prices.size();
    
    // error case
    if (ndays<=1) return 0;
    
    // Edge case
    // ---------
    // if the number of transactions is too many, it means we can make 
    // as many transactions as we can, that brings us the problem back to 
    // Best-Time-To-Buy-And-Sell-Stock-II which can be simply solve in O(n) 
    // by using a greedy approach.
    if(k > ndays/2){
        int sum = 0;
        for (int i=1; i<ndays; i++) {
            sum += max(prices[i] - prices[i-1], 0);
        }
        return sum;
    }
    
    //DP solution - O(kn) complexity 
    vector< vector<int> > dp (k+1, vector<int>( ndays+1, 0));
    
    for(int i=1; i<=k; i++) {
        int t = dp[i-1][0] - prices[0];
        for (int j=1; j <= ndays; j++) {
            dp[i][j] = max(dp[i][j-1], t + prices[j-1]);
            if ( j < ndays ) {
                t = max(t, dp[i-1][j] - prices[j]);
            }
        }
    }
    
    return dp[k][ndays];
    
}

// Time:  O(n)
// Space: O(1)
int StockTrading_cooldown_1(vector<int>& prices) {
    if (prices.empty()) {
        return 0;
    }
    vector<int> buy(2), sell(2), coolDown(2);
    buy[0] = -prices[0];
    for (int i = 1; i < prices.size(); ++i) {
        // Bought before or buy today.
        buy[i % 2] = max(buy[(i - 1) % 2], coolDown[(i - 1) % 2] - prices[i]);
        // Sell today.
        sell[i % 2] = buy[(i - 1) % 2] + prices[i];
        // Sold before yesterday or sold yesterday.
        coolDown[i % 2] = max(coolDown[(i - 1) % 2], sell[(i - 1) % 2]);
    }
    return max(coolDown[(prices.size() - 1) % 2], sell[(prices.size() - 1) % 2]);
}

// Time:  O(n)
// Space: O(n)
int StockTrading_cooldown_2(vector<int>& prices) {
    if (prices.empty()) {
        return 0;
    }
    vector<int> buy(prices.size()), sell(prices.size()), coolDown(prices.size());
    buy[0] = -prices[0];
    for (int i = 1; i < prices.size(); ++i) {
        // Bought before or buy today.
        buy[i] = max(buy[i - 1], coolDown[i - 1] - prices[i]);
        // Sell today.
        sell[i] = buy[i - 1] + prices[i];
        // Sold before yesterday or sold yesterday.
        coolDown[i] = max(coolDown[i - 1], sell[i - 1]);
    }
    return max(coolDown[prices.size() - 1], sell[prices.size() - 1]);
}

// Time:  O(n)
// Space: O(1)
int StockTrading_fee(vector<int>& prices, int fee) {
    int cash = 0, hold = -prices[0];
    for (int i = 1; i < prices.size(); ++i) {
        cash = max(cash, hold + prices[i] - fee);
        hold = max(hold, cash - prices[i]);
    }
    return cash;
}
```
 

