from textsummarizer.logging import logger
from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textsummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textsummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed successfully <<<<<< \n\n\n x=================x")  

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed successfully <<<<<< \n\n\n x=================x")  

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed successfully <<<<<< \n\n\n x=================x")  

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed successfully <<<<<< \n\n\n x=================x")  

except Exception as e:
    logger.exception(e)
    raise e
