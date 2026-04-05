import pandas as pd
from rules import rule_based_score
from detector import AnomalyDetector
from decision import make_decision
from explain import generate_explanation
from override import request_override


def main():
    df = pd.read_csv("data/traffic.csv")

    detector = AnomalyDetector()
    detector.train(df)
    
    with open("firewall_log.txt", "w") as log_file:
        log_file.write("Adaptive Firewall Log\n")
        log_file.write("=" * 60 + "\n")


    print("=" * 60)
    print("Adaptive Firewall Prototype")
    print("=" * 60)

    for _, row in df.iterrows():
        event = row.to_dict()

        rule_score, reasons = rule_based_score(event)
        ai_score = detector.predict_risk(event)
        total_score = rule_score + ai_score

        decision = make_decision(total_score)
        explanation = generate_explanation(decision, reasons, ai_score)

        print("\nEvent:")
        print(event)
        print(f"Rule Score: {rule_score}")
        print(f"AI Score: {ai_score}")
        print(f"Total Score: {total_score}")
        print(explanation)

        with open("firewall_log.txt", "a") as log_file:
            log_file.write("Event:\n")
            log_file.write(str(event) + "\n")
            log_file.write(f"Rule Score: {rule_score}\n")
            log_file.write(f"AI Score: {ai_score}\n")
            log_file.write(f"Total Score: {total_score}\n")
            log_file.write(explanation + "\n")
            log_file.write("-" * 60 + "\n")

        if decision == "VERIFY":
            print("\nTrying temporary override...")
            override_result = request_override(
                user_verified=True,
                feature_name="restricted_app_access"
            )
            print(override_result["message"])

            with open("firewall_log.txt", "a") as log_file:
                log_file.write("Override Attempt:\n")
                log_file.write(override_result["message"] + "\n")
                log_file.write("=" * 60 + "\n")


if __name__ == "__main__":
    main()