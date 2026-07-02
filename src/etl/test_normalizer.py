from normalizer import normalize_company_id, normalize_year

print(normalize_company_id(" abb "))
print(normalize_company_id("tcs"))

print(normalize_year("Mar-13"))
print(normalize_year("Mar 2014"))
print(normalize_year("Dec 2012"))