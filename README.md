# SPasswords
## Lightweight script to generate strong passwords

### Using the `Random` module  

![image alt](https://github.com/ousax/SPasswords/blob/a168df1d431a92da0b772223f9ab097047f568b2/passgg.png)

### Using the `Secrets` module

![image alt](https://github.com/ousax/SPasswords/blob/52754040aa987f18b567995476d9ec9ba9434842/passSecrets.png)

# Available options  

| Argument      | Help Description                                                                 | Type   | Required | Default | Choices     |
|---------------|----------------------------------------------------------------------------------|--------|----------|---------|-------------|
| `-plen`       | The password's length [10 by default]                                            | int    | No       | 10      | –           |
| `-sf`         | Save to a file                                                                   | str    | No       | None    | –           |
| `-pNumber`    | Number of passwords to generate                                                  | int    | No       | 1000    | –           |
| `-all_`       | Use digits, strings, punctuation                                                 | int    | No       | 0       | 0, 1        |
| `-eXD`        | Exclude digits [0] to exclude, [1] to include digits                             | int    | No       | 1       | 0, 1        |
| `-eXP`        | Exclude/Include punctuations [0] exclude, [1] include                            | int    | No       | 1       | 0, 1        |
| `-eXS`        | Exclude/Include letters [lower, upper case] [0] exclude, [1] include             | int    | No       | 1       | 0, 1        |
| `-prefix_`    | Add a prefix to the passwords (e.g., fb, tiktok, gmail, twitter, etc.)           | str    | No       | ""      | –           |
| `-passCheck`  | Check the complexity of the password                                             | int    | No       | –       | 0, 1        |
| `-useSecrets` | Use `secrets` instead of `random` for better randomness (can be slower)          | int    | No       | n       | Hex, Choice, UrlSafe, n        |


# Requirements 
- rich
- pyfiglet

# Install

```bash
git clone https://github.com/ousax/SPasswords.git ; 
cd SPasswords;
pip -r install requirements;
chmod +x StrongPasswords.py;
python3 StrongPasswords.py -h
```



# Usage 
- python3 StrongPasswords.py -plen 20 -sf googlePass -pNumber 10 -eXD 1 -eXS 1 -eXP 0 -prefix_ google -useSecret 1
- python3 StrongPasswords.py -plen 20 -sf googlePass -pNumber 10 -eXD 1 -eXS 1 -eXP 0 -prefix_ google -useSecret 0    
