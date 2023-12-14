-- This script ranks country origins of bands based on the number of fans
SELECT origin, sum(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
