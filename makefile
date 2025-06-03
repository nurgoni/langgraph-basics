run-agent:
	PYTHONPATH=src python3 src/langg/run_agent.py

run-streamlit:
	PYTHONPATH=src streamlit run src/langg/streamlit_app.py