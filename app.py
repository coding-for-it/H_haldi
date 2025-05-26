from fastapi import FastAPI, Response, HTTPException
from adv_analysis.KPI1 import get_attribute_frequency_chart
from adv_analysis.KPI2 import get_attribute_frequency_chart_kpi2_with_sentiment
from adv_analysis.KPI3 import get_kpi3_sheet1_campaign_timeline_chart
from fastapi import FastAPI
from adv_analysis.KPI4 import router as kpi4_router
from adv_analysis.KPI5 import get_kpi5_chart
from fastapi import FastAPI, UploadFile, File, HTTPException
from adv_analysis.KPI6 import read_kpi6_excel
import numpy as np
from adv_analysis.KPI7 import get_brand_personality_radar
from fastapi.responses import JSONResponse
from adv_analysis.KPI8 import get_kpi8_dashboard_chart_and_data
from adv_analysis.KPI9 import get_kpi9_reviews_data
from adv_analysis.KPI10 import get_comparison_sheet_sections
from fastapi.responses import HTMLResponse
from adv_analysis.KPI11 import get_docx_file_response
from adv_analysis.KPI12 import analyze_kpi12_data
from adv_analysis.KPI13 import get_conversion_funnel_chart_improved
from adv_analysis.KPI14 import analyze_data
from adv_analysis.KPI15 import get_sheet2_data
from adv_analysis.KPI16 import get_value_perception_charts
from adv_analysis.KPI17 import get_sheet1_data
from adv_analysis.KPI18 import get_kpi18_sheet5_data
from adv_analysis.KPI19 import get_kpi19_sheet1_data
from adv_analysis.KPI20 import get_kpi20_sheet2_data
from adv_analysis.KPI21 import get_kpi21_sheet1_data
from adv_analysis.KPI22 import get_category_pie_chart
from adv_analysis.KPI23 import get_kpi23_sheet1_data
from adv_analysis.KPI24 import  get_kpi24_sheet3_data,  get_kpi24_qualitative_assessment_details
from adv_analysis.KPI25 import get_crisis_sentiment_trends_chart


from fastapi.responses import StreamingResponse

app = FastAPI()
app.include_router(kpi4_router)

#ppd = PostPurchaseDissonance()

# Include KPI1 router
@app.get("/kpi1/attribute-frequency")
def attribute_frequency_kpi():
    img_bytes = get_attribute_frequency_chart()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")


@app.get("/kpi2/sentiment-breakdown")
def sentiment_breakdown_kpi():
    img_bytes = get_attribute_frequency_chart_kpi2_with_sentiment()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi3/sheet2-chart")
def kpi3_sheet2_chart():
    img_bytes = get_kpi3_sheet1_campaign_timeline_chart()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")

# Include the KPI-4 router
@app.get("/")
def main():
    return {"message": "Main function called"}

@app.get("/kpi5/chart")
def kpi5_chart():
    img_bytes = get_kpi5_chart()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi6/data")
def get_kpi6_data():
    df = read_kpi6_excel()
    if df is None:
        raise HTTPException(status_code=400, detail="Error reading Excel file")
    # Replace NaN and infinite values with None
    df = df.replace([np.nan, np.inf, -np.inf], None)
    return df.to_dict(orient="records")

@app.get("/kpi7/brand-personality-radar")
def brand_personality_radar_kpi():
    img_bytes = get_brand_personality_radar()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi8/dashboard-image")
def get_dashboard_image():
    """Endpoint to get dashboard chart as PNG"""
    img_bytes, _ = get_kpi8_dashboard_chart_and_data()
    if not img_bytes:
        raise HTTPException(404, "No data available to generate chart")
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi8/dashboard-data")
def get_dashboard_data():
    """Endpoint to get Sheet3 data and chart URL"""
    img_bytes, df = get_kpi8_dashboard_chart_and_data()
    
    if df.empty:
        raise HTTPException(404, "No data available in Sheet3")
    
    return JSONResponse({
        "chart_url": "/kpi8/dashboard-image",
        "sheet3_data": df.replace({np.nan: None}).to_dict(orient="records")
    })

@app.get("/kpi9/reviews")
def kpi9_reviews():
    try:
        data = get_kpi9_reviews_data()
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading KPI-9 file: {e}")

@app.get("/kpi10/comparison-full")
def comparison_full():
    try:
        data = get_comparison_sheet_sections()
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing Comparison sheet: {e}")

@app.get("/kpi11/doc-file")
def serve_docx():
    response = get_docx_file_response()
    if response is None:
        raise HTTPException(status_code=404, detail="File not found")
    return response

@app.get("/kpi12/results")
def get_kpi12_results():
    results = analyze_kpi12_data()
    if not results:
        raise HTTPException(status_code=404, detail="KPI data not found")
    return results

@app.get("/kpi13/conversion-funnel")
def conversion_funnel_kpi():
    img_bytes = get_conversion_funnel_chart_improved()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi14/results")
def get_kpi12_results():
    results = analyze_data()
    
    if not results:
        raise HTTPException(
            status_code=404,
            detail="KPI data not found",
            headers={"X-Error": "KPI12_DATA_MISSING"}
        )
        
    return {
        "status": "success",
        "results": results,
        "count": len(results)
    }

@app.get("/kpi15/sheet2")
def get_kpi15_sheet2():
    results = get_sheet2_data()
    if not results:
        raise HTTPException(
            status_code=404,
            detail="No data found in Sheet2 of KPI-15.xlsx",
            headers={"X-Error": "SHEET2_DATA_MISSING"}
        )
    return {
        "status": "success",
        "results": results,
        "count": len(results)
    }

@app.get("/kpi16/value-perception-charts")
def value_perception_kpi():
    img_bytes = get_value_perception_charts()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi17/sheet1")
def get_kpi17_sheet1():
    try:
        results = get_sheet1_data()
        if not results:
            raise HTTPException(
                status_code=404,
                detail="No data found in Sheet1 of KPI-17.xlsx",
                headers={"X-Error": "SHEET1_DATA_MISSING"}
            )
        return {
            "status": "success",
            "results": results,
            "count": len(results)
        }
    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Excel file not found",
            headers={"X-Error": "FILE_NOT_FOUND"}
        )

@app.get("/kpi18/sheet5")
def get_kpi18_sheet5():
    results = get_kpi18_sheet5_data()
    if not results:
        raise HTTPException(
            status_code=404,
            detail="No data found in Sheet5 of KPI-18.xlsx",
            headers={"X-Error": "SHEET5_DATA_MISSING"}
        )
    return {
        "status": "success",
        "results": results,
        "count": len(results)
    }

@app.get("/kpi19/sheet1")
def get_kpi19_sheet1():
    results = get_kpi19_sheet1_data()
    if not results:
        raise HTTPException(
            status_code=404,
            detail="No data found in Sheet1 of KPI-19.xlsx",
            headers={"X-Error": "SHEET1_DATA_MISSING"}
        )
    return {
        "status": "success",
        "results": results,
        "count": len(results)
    }

@app.get("/kpi20/sheet2")
def get_kpi20_sheet2():
    results = get_kpi20_sheet2_data()
    if not results:
        raise HTTPException(
            status_code=404,
            detail="No data found in Sheet2 of KPI-20.xlsx",
            headers={"X-Error": "SHEET2_DATA_MISSING"}
        )
    return {
        "status": "success",
        "results": results,
        "count": len(results)
    }

@app.get("/kpi21/sheet1")
def get_kpi21_sheet1():
    results = get_kpi21_sheet1_data()
    if not results:
        raise HTTPException(
            status_code=404,
            detail="No data found in Sheet1 of KPI-21.xlsx",
            headers={"X-Error": "SHEET1_DATA_MISSING"}
        )
    return {
        "status": "success",
        "results": results,
        "count": len(results)
    }

@app.get("/kpi22/category-pie-chart")
def category_pie_chart_kpi():
    img_bytes = get_category_pie_chart()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")

@app.get("/kpi23/sheet1")
def get_kpi23_sheet1():
    results = get_kpi23_sheet1_data()
    if not results:
        raise HTTPException(
            status_code=404,
            detail="No data found in Sheet1 of KPI-23.xlsx",
            headers={"X-Error": "SHEET1_DATA_MISSING"}
        )
    return {
        "status": "success",
        "results": results,
        "count": len(results)
    }


"""@app.get("/kpi24/sheet3")
def get_kpi24_sheet3():
    results = get_kpi24_sheet3_data()
    if not results:
        raise HTTPException(
            status_code=404,
            detail="No valid data found in Sheet3 of KPI-24.xlsx",
            headers={"X-Error": "SHEET3_DATA_MISSING"}
        )
    return {
        "status": "success",
        "results": results,
        "count": len(results)
    }"""

@app.get("/kpi24/qualitative-assessment")
def get_kpi24_qualitative_assessment():
    results = get_kpi24_qualitative_assessment_details()
    if not results:
        raise HTTPException(
            status_code=404,
            detail="No qualitative assessment details found in Sheet3 of KPI-24.xlsx",
            headers={"X-Error": "QUALITATIVE_ASSESSMENT_MISSING"}
        )
    return {
        "status": "success",
        "results": results,
        "count": len(results)
    }

@app.get("/kpi25/Brand Resilience Score")
def sentiment_breakdown_kpi():
    img_bytes = get_crisis_sentiment_trends_chart()
    if not img_bytes:
        return {"message": "No data available to plot"}
    return Response(content=img_bytes, media_type="image/png")