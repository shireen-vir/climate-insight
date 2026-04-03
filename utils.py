class ClimateInsightException(Exception):
    pass

def calculate_emissions(data):
    return sum(data)

def analyze_data(data):
    emissions = calculate_emissions(data)
    return emissions

def main():
    try:
        data = [10, 20, 30]
        result = analyze_data(data)
        print(f'Emissions: {result}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

if __name__ == '__main__':
    main()