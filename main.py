import csv
import matplotlib.pyplot as plt
from random import shuffle, sample
from bloomfilter import BloomFilter

# Lần đầu chạy, đọc Phishing URLs và lưu vào biến toàn cục
def load_phishing_urls():
    with open('Phishing URLs.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        return [row[0] for row in reader if row]

PHISHING_LIST = load_phishing_urls()

def test_and_plot(num_tests=10):
    rates = []
    for i in range(num_tests):
        # Re-run your existing code
        n = len(PHISHING_LIST)
        p = 0.05
        bloomf = BloomFilter(n, p)
        for url in PHISHING_LIST:
            bloomf.add(url)

        with open('URL dataset.csv', 'r', encoding='utf-8') as f:
            dataset_list = [row[0] for row in csv.reader(f) if row]

        test_urls = sample(dataset_list, 100)
        shuffle(test_urls)

        false_positive_count = 0
        for url in test_urls:
            if bloomf.check(url) and url not in PHISHING_LIST:
                false_positive_count += 1

        fpr = (false_positive_count / len(test_urls)) * 100
        rates.append(fpr)

    plt.plot(range(1, num_tests + 1), rates, marker='o', label='False Positive Rate')
    plt.axhline(y=5, color='r', linestyle='--', label='p=0.05')  # Vẽ đường ngang
    plt.xlabel("Test iteration")
    plt.ylabel("False positive rate (%)")
    plt.title("False positive rate vs. test iteration (p=0.05)")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    test_and_plot()