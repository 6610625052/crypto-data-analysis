UPDATE coins SET category = 'Layer 1' WHERE name = 'Bitcoin';
UPDATE coins SET category = 'Layer 1' WHERE name = 'Ethereum';
UPDATE coins SET category = 'Stablecoin' WHERE name = 'Tether';
UPDATE coins SET category = 'Layer 1' WHERE name = 'BNB';
UPDATE coins SET category = 'Payment' WHERE name = 'XRP';
UPDATE coins SET category = 'Stablecoin' WHERE name = 'USDC';
UPDATE coins SET category = 'Layer 1' WHERE name = 'Solana';
UPDATE coins SET category = 'Layer 1' WHERE name = 'Cardano';
UPDATE coins SET category = 'Meme Coin' WHERE name = 'Dogecoin';
UPDATE coins SET category = 'Layer 1' WHERE name = 'Toncoin';
SELECT category, AVG(current_price) AS avg_price
FROM coins
WHERE category IS NOT NULL
GROUP BY category;
SELECT name, current_price, market_cap
FROM coins
ORDER BY market_cap DESC
LIMIT 5;
