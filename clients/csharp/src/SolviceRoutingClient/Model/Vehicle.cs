/* 
 * Solvice API
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.0.0-oas3
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */
using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = SolviceRoutingClient.Client.SwaggerDateConverter;

namespace SolviceRoutingClient.Model
{
    /// <summary>
    /// Vehicle
    /// </summary>
    [DataContract]
        public partial class Vehicle :  IEquatable<Vehicle>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Vehicle" /> class.
        /// </summary>
        /// <param name=""> (required).</param>
        /// <param name=""> (required).</param>
        /// <param name="">.</param>
        /// <param name="">.</param>
        /// <param name="">.</param>
        /// <param name="">.</param>
        /// <param name="">.</param>
        /// <param name="">.</param>
        public Vehicle(string  = default(string), string  = default(string), string  = default(string), BigDecimal  = default(BigDecimal), BigDecimal  = default(BigDecimal), int?  = default(int?), int?  = default(int?), List<string>  = default(List<string>))
        {
            // to ensure "" is required (not null)
            if ( == null)
            {
                throw new InvalidDataException(" is a required property for Vehicle and cannot be null");
            }
            else
            {
                this.Name = ;
            }
            // to ensure "" is required (not null)
            if ( == null)
            {
                throw new InvalidDataException(" is a required property for Vehicle and cannot be null");
            }
            else
            {
                this.Startlocation = ;
            }
            this.Endlocation = ;
            this.Capacity = ;
            this.Capacity2 = ;
            this.Shiftstart = ;
            this.Shiftend = ;
            this.Type = ;
        }
        
        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name="name", EmitDefaultValue=false)]
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets Startlocation
        /// </summary>
        [DataMember(Name="startlocation", EmitDefaultValue=false)]
        public string Startlocation { get; set; }

        /// <summary>
        /// Gets or Sets Endlocation
        /// </summary>
        [DataMember(Name="endlocation", EmitDefaultValue=false)]
        public string Endlocation { get; set; }

        /// <summary>
        /// Gets or Sets Capacity
        /// </summary>
        [DataMember(Name="capacity", EmitDefaultValue=false)]
        public BigDecimal Capacity { get; set; }

        /// <summary>
        /// Gets or Sets Capacity2
        /// </summary>
        [DataMember(Name="capacity2", EmitDefaultValue=false)]
        public BigDecimal Capacity2 { get; set; }

        /// <summary>
        /// Gets or Sets Shiftstart
        /// </summary>
        [DataMember(Name="shiftstart", EmitDefaultValue=false)]
        public int? Shiftstart { get; set; }

        /// <summary>
        /// Gets or Sets Shiftend
        /// </summary>
        [DataMember(Name="shiftend", EmitDefaultValue=false)]
        public int? Shiftend { get; set; }

        /// <summary>
        /// Gets or Sets Type
        /// </summary>
        [DataMember(Name="type", EmitDefaultValue=false)]
        public List<string> Type { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class Vehicle {\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  Startlocation: ").Append(Startlocation).Append("\n");
            sb.Append("  Endlocation: ").Append(Endlocation).Append("\n");
            sb.Append("  Capacity: ").Append(Capacity).Append("\n");
            sb.Append("  Capacity2: ").Append(Capacity2).Append("\n");
            sb.Append("  Shiftstart: ").Append(Shiftstart).Append("\n");
            sb.Append("  Shiftend: ").Append(Shiftend).Append("\n");
            sb.Append("  Type: ").Append(Type).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as Vehicle);
        }

        /// <summary>
        /// Returns true if Vehicle instances are equal
        /// </summary>
        /// <param name="input">Instance of Vehicle to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(Vehicle input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.Startlocation == input.Startlocation ||
                    (this.Startlocation != null &&
                    this.Startlocation.Equals(input.Startlocation))
                ) && 
                (
                    this.Endlocation == input.Endlocation ||
                    (this.Endlocation != null &&
                    this.Endlocation.Equals(input.Endlocation))
                ) && 
                (
                    this.Capacity == input.Capacity ||
                    (this.Capacity != null &&
                    this.Capacity.Equals(input.Capacity))
                ) && 
                (
                    this.Capacity2 == input.Capacity2 ||
                    (this.Capacity2 != null &&
                    this.Capacity2.Equals(input.Capacity2))
                ) && 
                (
                    this.Shiftstart == input.Shiftstart ||
                    (this.Shiftstart != null &&
                    this.Shiftstart.Equals(input.Shiftstart))
                ) && 
                (
                    this.Shiftend == input.Shiftend ||
                    (this.Shiftend != null &&
                    this.Shiftend.Equals(input.Shiftend))
                ) && 
                (
                    this.Type == input.Type ||
                    this.Type != null &&
                    this.Type.SequenceEqual(input.Type)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Name != null)
                    hashCode = hashCode * 59 + this.Name.GetHashCode();
                if (this.Startlocation != null)
                    hashCode = hashCode * 59 + this.Startlocation.GetHashCode();
                if (this.Endlocation != null)
                    hashCode = hashCode * 59 + this.Endlocation.GetHashCode();
                if (this.Capacity != null)
                    hashCode = hashCode * 59 + this.Capacity.GetHashCode();
                if (this.Capacity2 != null)
                    hashCode = hashCode * 59 + this.Capacity2.GetHashCode();
                if (this.Shiftstart != null)
                    hashCode = hashCode * 59 + this.Shiftstart.GetHashCode();
                if (this.Shiftend != null)
                    hashCode = hashCode * 59 + this.Shiftend.GetHashCode();
                if (this.Type != null)
                    hashCode = hashCode * 59 + this.Type.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }
}
