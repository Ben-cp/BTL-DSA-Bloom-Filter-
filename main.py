import csv
import matplotlib.pyplot as plt
import time
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
    times = []
    for i in range(num_tests):
        start_time = time.time()
        
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
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        times.append(elapsed_time)

    fig, ax1 = plt.subplots()

    color = 'tab:blue'
    ax1.set_xlabel('Test iteration')
    ax1.set_ylabel('False positive rate (%)', color=color)
    ax1.plot(range(1, num_tests + 1), rates, marker='o', color=color, label='False Positive Rate')
    ax1.axhline(y=5, color='r', linestyle='--', label='p=0.05')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.legend(loc='upper left')

    ax2 = ax1.twinx()  
    color = 'tab:green'
    ax2.set_ylabel('Time (seconds)', color=color)
    ax2.plot(range(1, num_tests + 1), times, marker='x', color=color, label='Execution Time')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.legend(loc='upper right')

    plt.title("False Positive Rate and Execution Time vs. Test Iteration (p=0.05)")
    fig.tight_layout()  
    plt.show()

if __name__ == "__main__":
    test_and_plot()