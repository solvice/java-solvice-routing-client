/*
 * OnRoute API
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.1.3
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.solvice.routing.api.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.solvice.routing.api.client.model.Visit;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * RoutingSolution
 */

public class RoutingSolution {

  @SerializedName("solution")
  private Map<String, List<Visit>> solution = null;
  public RoutingSolution solution(Map<String, List<Visit>> solution) {
    this.solution = solution;
    return this;
  }

  
  public RoutingSolution putSolutionItem(String key, List<Visit> solutionItem) {
    if (this.solution == null) {
      this.solution = new HashMap<String, List<Visit>>();
    }
    this.solution.put(key, solutionItem);
    return this;
  }
  /**
  * Get solution
  * @return solution
  **/
  @Schema(description = "")
  public Map<String, List<Visit>> getSolution() {
    return solution;
  }
  public void setSolution(Map<String, List<Visit>> solution) {
    this.solution = solution;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RoutingSolution routingSolution = (RoutingSolution) o;
    return Objects.equals(this.solution, routingSolution.solution);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(solution);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RoutingSolution {\n");
    
    sb.append("    solution: ").append(toIndentedString(solution)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}