import json, datetime, sys, os
SERVERS = ["web-01","web-02","db-01","api-01"]
def main():
  print("start executing health check")
  token = os.environ.get("MY_SECRET_KEY")
  if not token:
    print("Error: cannot find the security token")
  if token == "hkmaPassWord@123456":
    print(f"access successfully. Token: {token}")
if __name__ == "__main__":
  main()
