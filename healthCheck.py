improt json, datetime, sys
SERVERS = ["web-01","web-02","db-01","api-01"]
def main():
  results = []
  for server in SERVERS:
    status = "UP"
    results.append({"server":server,"status":status})
    print(f"{server}:{status}")

  report = {
    "timestamp":datetime.datetime.now().isoformat(),
    "total":len(results),
    "up":sum(1 for r in results if r["status"] == "UP"),
    "down":sum(1 for r in results if r["status"] == "DOWN"),
    "results":results
  }

  with open("health-report.json","w") as f:
    json.dump(report, f, indent=2)
  percent = {report['up']}/{report['total']} * 100
  print(f"\nReport: {percent}% servers UP")

if __name__ == "__main__":
  main()
