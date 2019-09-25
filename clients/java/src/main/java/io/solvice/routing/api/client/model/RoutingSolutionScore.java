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
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;

/**
 * The score of a solution shows how good this solution is w.r.t all the constraints.
 */
@Schema(description = "The score of a solution shows how good this solution is w.r.t all the constraints.")
public class RoutingSolutionScore {

  @SerializedName("hardScore")
  private Integer hardScore = null;

  @SerializedName("mediumScore")
  private Integer mediumScore = null;

  @SerializedName("softScore")
  private Integer softScore = null;

  @SerializedName("feasible")
  private Boolean feasible = null;
  public RoutingSolutionScore hardScore(Integer hardScore) {
    this.hardScore = hardScore;
    return this;
  }

  

  /**
  * The score of the constraints that are hard. This should be 0 in order to be feasible.
  * @return hardScore
  **/
  @Schema(description = "The score of the constraints that are hard. This should be 0 in order to be feasible.")
  public Integer getHardScore() {
    return hardScore;
  }
  public void setHardScore(Integer hardScore) {
    this.hardScore = hardScore;
  }
  public RoutingSolutionScore mediumScore(Integer mediumScore) {
    this.mediumScore = mediumScore;
    return this;
  }

  

  /**
  * The score of the constraints that are medium.
  * @return mediumScore
  **/
  @Schema(description = "The score of the constraints that are medium.")
  public Integer getMediumScore() {
    return mediumScore;
  }
  public void setMediumScore(Integer mediumScore) {
    this.mediumScore = mediumScore;
  }
  public RoutingSolutionScore softScore(Integer softScore) {
    this.softScore = softScore;
    return this;
  }

  

  /**
  * The score of the constraints that are soft.
  * @return softScore
  **/
  @Schema(description = "The score of the constraints that are soft.")
  public Integer getSoftScore() {
    return softScore;
  }
  public void setSoftScore(Integer softScore) {
    this.softScore = softScore;
  }
  public RoutingSolutionScore feasible(Boolean feasible) {
    this.feasible = feasible;
    return this;
  }

  

  /**
  * Feasibility check on hard constraints. Check unresolved parameter if you cannot reach feasibility.
  * @return feasible
  **/
  @Schema(description = "Feasibility check on hard constraints. Check unresolved parameter if you cannot reach feasibility.")
  public Boolean isFeasible() {
    return feasible;
  }
  public void setFeasible(Boolean feasible) {
    this.feasible = feasible;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RoutingSolutionScore routingSolutionScore = (RoutingSolutionScore) o;
    return Objects.equals(this.hardScore, routingSolutionScore.hardScore) &&
        Objects.equals(this.mediumScore, routingSolutionScore.mediumScore) &&
        Objects.equals(this.softScore, routingSolutionScore.softScore) &&
        Objects.equals(this.feasible, routingSolutionScore.feasible);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(hardScore, mediumScore, softScore, feasible);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RoutingSolutionScore {\n");
    
    sb.append("    hardScore: ").append(toIndentedString(hardScore)).append("\n");
    sb.append("    mediumScore: ").append(toIndentedString(mediumScore)).append("\n");
    sb.append("    softScore: ").append(toIndentedString(softScore)).append("\n");
    sb.append("    feasible: ").append(toIndentedString(feasible)).append("\n");
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